from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import autocorrelation_plot
import matplotlib.pyplot as plt

from Data import Data

data = Data('GS')
data_FT = data.get_close_data()

series = data_FT['price']
model = ARIMA(series, order=(5, 1, 0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

ax = autocorrelation_plot(series)
fig = ax.get_figure()
fig.savefig(fname='../assets/ARIMA_as_a_feature.png')
fig.show()
# plt.figure(figsize=(10, 7), dpi=80)
# plt.show()

if __name__ == "__main__":
    pass
