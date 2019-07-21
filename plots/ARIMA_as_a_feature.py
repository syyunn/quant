from tqdm import tqdm
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from pandas.plotting import autocorrelation_plot
import matplotlib.pyplot as plt
from Data import Data

# Data prep
ticker = 'GS'
data = Data('GS')
data_FT = data.get_close_data()

series = data_FT[ticker]

# Check Auto-correlation
model = ARIMA(series, order=(5, 1, 0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

ax = autocorrelation_plot(series)
fig = ax.get_figure()
fig.savefig(fname='../assets/ARIMA_as_a_feature.png')
fig.show()

# Check the Prediction Power of ARIMA
X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()

for t in tqdm(range(len(test))):
    model = ARIMA(history, order=(5,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)
error = mean_squared_error(test, predictions)

print('Test MSE: %.3f' % error)

plt.figure(figsize=(12, 6), dpi=100)
plt.plot(test, label='Real')
plt.plot(predictions, color='red', label='Predicted')
plt.xlabel('Days')
plt.ylabel('USD')
plt.title('Figure 5: ARIMA model on GS stock')
plt.legend()
plt.savefig('../assets/ARIMA_model_on_GS_stock.png')
plt.show()

if __name__ == "__main__":
    pass
