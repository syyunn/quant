from statsmodels.tsa.arima_model import ARIMA

from Data import Data

data = Data('GS')
data_FT = data.get_close_data()

series = data_FT['price']
model = ARIMA(series, order=(5, 1, 0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

if __name__ == "__main__":
    pass
