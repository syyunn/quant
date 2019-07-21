from Data import Data
from utils import merge_n_dfs
from interest_rate.LIBOR import get_libor

# # Other companies

# Goldman Sachs
data_GS = Data('GS')
data_GS = data_GS.get_close_data()

# JPMorgan Chase
data_JPM = Data('JPM')
data_JPM = data_JPM.get_close_data()

# Morgan Stanley
data_MS = Data('MS')
data_MS = data_MS.get_close_data()

# Merge n different assests
dfs = [data_GS, data_JPM, data_MS]
merge = merge_n_dfs(dfs, common_col="Date")

# Merge LIBOR to Stock data
libor = get_libor()
merge = merge_n_dfs([merge, libor], common_col="Date")

if __name__ == "__main__":
    pass
