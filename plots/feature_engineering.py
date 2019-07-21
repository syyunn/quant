from Data import Data

# Data preparation
data = Data('GS')
data_FT = data.get_close_data()


print('Total dataset has {} samples, and {} features.'.format(data_FT.shape[0], \
                                                              data_FT.shape[1]))

if __name__ == "__main__":
    pass
