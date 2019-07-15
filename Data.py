import multiprocessing as mp

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

        data_dict = {'Date': dates[sg_start:], self.code: prices[sg_start:]}

        df = pd.DataFrame(data_dict)

        return df


if __name__ == "__main__":
    data = Data('GS')
    df = data.get_close_data()
    print(df.head(3))

