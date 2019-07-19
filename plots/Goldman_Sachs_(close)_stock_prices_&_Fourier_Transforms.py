import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Data import Data

# Data preparation
data = Data('GS')
data_FT = data.get_close_data()


close_fft = np.fft.fft(np.asarray(data_FT['price'].tolist()))
fft_df = pd.DataFrame({'fft': close_fft})

# # These are not used in plotting
# fft_df['absolute'] = fft_df['fft'].apply(lambda x: np.abs(x))
# fft_df['angle'] = fft_df['fft'].apply(lambda x: np.angle(x))

plt.figure(figsize=(14, 7), dpi=100)
fft_list = np.asarray(fft_df['fft'].tolist())

# Plotting Fourier Transforms
for num_ in [3,
             6,
             9,
             100]:
    fft_list_m10 = np.copy(fft_list)
    fft_list_m10[num_:-num_] = 0
    plt.plot(np.fft.ifft(fft_list_m10),
             label='Fourier transform with {} components'.format(num_))

# Plot the original Goldman Sachs prices
plt.plot(data_FT['price'],  label='Real')

plt.xlabel('Days')
plt.ylabel('USD')

plt.title('Figure 3: Goldman Sachs (close) stock prices & Fourier transforms')

plt.savefig(
    '../assets/Goldman_Sachs_(close)_stock_prices_&_Fourier_Transforms.png')

plt.legend()

plt.show()

if __name__ == "__main__":
    pass
