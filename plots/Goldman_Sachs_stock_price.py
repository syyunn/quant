import datetime
import matplotlib.pyplot as plt

from Data import Data

data = Data('GS')
df = data.get_close_data()

plt.figure(figsize=(14, 5), dpi=100)
plt.plot(df['Date'], df['GS'], label='Goldman Sachs stock')

plt.vlines(datetime.date(2016, 4, 20),
           0,
           270,
           linestyles='--',
           colors='gray',
           label='Train/Test data cut-off')

plt.xlabel('Date')
plt.ylabel('USD')
plt.title('Figure 2: Goldman Sachs stock price')
plt.savefig('assets/Goldman_Sachs_stock_price.png')
plt.legend()
plt.show()

if __name__ == "__main__":
    pass
