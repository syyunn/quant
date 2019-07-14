import datetime

import matplotlib.pyplot as plt

from utils import load_pickle

pickle_path = "data/nyse_gs.pkl"
data = load_pickle(pickle_path)


# plt plotting
plt.figure(figsize=(14, 5), dpi=100)
plt.plot(data['dates'], data['prices'], label='Goldman Sachs stock')
plt.vlines(datetime.date(2016, 4, 20), 0, 270, linestyles='--', colors='gray', label='Train/Test data cut-off')
plt.xlabel('Date')
plt.ylabel('USD')
plt.title('Figure 2: Goldman Sachs stock price')
plt.savefig('assests/nyse_gs.png')
plt.legend()
plt.show()

if __name__ == "__main__":
    pass
