import numpy as np

import pandas as pd
import yfinance as yf

from utils import parser, pickle_object

from Constants import sg_start  # Boris has used data from 2009-12-31


class Data:
    def __init__(self,
                 code):
        self.code = code
        self.ticker = yf.Ticker(code)

        self.hist = self.ticker.history(period="max")

    def get_close_data(self):
        hist_close = self.hist["Close"]
        keys = hist_close.keys()

        dates = []
        prices = []

        for key in keys:
            date = parser(key._date_repr)
            price = hist_close[key]
            dates.append(date)
            prices.append(price)

        data_dict = {'Date': dates[sg_start:], 'price': prices[sg_start:]}

        df = pd.DataFrame(data_dict)

        return df


def get_technical_indicators(dataset):
    # Create 7 and 21 days Moving Average
    dataset['ma7'] = dataset['price'].rolling(window=7).mean()
    dataset['ma21'] = dataset['price'].rolling(window=21).mean()

    # Create MACD
    dataset['26ema'] = dataset['price'].ewm(span=26).mean()
    dataset['12ema'] = dataset['price'].ewm(span=12).mean()
    dataset['MACD'] = (dataset['12ema'] - dataset['26ema'])

    # Create Bollinger Bands
    dataset['20sd'] = dataset['price'].rolling(20).std()
    dataset['upper_band'] = dataset['ma21'] + (dataset['20sd'] * 2)
    dataset['lower_band'] = dataset['ma21'] - (dataset['20sd'] * 2)

    # Create Exponential moving average
    dataset['ema'] = dataset['price'].ewm(com=0.5).mean()

    # Create Momentum
    dataset['momentum'] = dataset['price'] - 1

    # Create Log Momentum
    dataset['log_momentum'] = np.log(dataset['momentum'])

    return dataset


if __name__ == "__main__":
    # Chapter 3.0
    data = Data('GS')
    df = data.get_close_data()
    # print(df.head(3))

    # Chapter 3.2
    dataset_ti_df = get_technical_indicators(df)
    print(dataset_ti_df[20:].head())

    print(dataset_ti_df[20:]['log_momentum'].head())

