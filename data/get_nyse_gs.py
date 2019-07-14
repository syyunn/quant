import yfinance as yf
from utils import parser, pickle_object

from Constants import sg_start  # Boris has used data from 2009-12-31

gs = yf.Ticker("GS")

hist = gs.history(period="max")
hist_close = hist['Close']
keys = hist_close.keys()  # keys are Timestamp objects that refers to dates

dates = []
prices = []
for idx, key in enumerate(keys):
    date = parser(key._date_repr)
    # print(idx, date)
    price = hist_close[key]
    dates.append(date)
    prices.append(price)

# pickle to store data
data = dict()
data['dates'] = dates[sg_start:]
data['prices'] = prices[sg_start:]

pickle_path = 'nyse_gs.pkl'
pickle_object(data, pickle_path)

if __name__ == "__main__":
    pass
