from collections import deque

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
fft_df['absolute'] = fft_df['fft'].apply(lambda x: np.abs(x))
# fft_df['angle'] = fft_df['fft'].apply(lambda x: np.angle(x))

items = deque(np.asarray(fft_df['absolute'].tolist()))
items.rotate(int(np.floor(len(fft_df)/2)))
plt.figure(figsize=(10, 7), dpi=80)
plt.stem(items)
plt.title('Figure 4: Components of Fourier transforms')
plt.savefig(
    '../assets/Components_of_Fourier_transforms.png')
plt.show()

if __name__ == "__main__":
    pass
