import datetime
import pickle

import pandas


def parser(x):
    return datetime.datetime.strptime(x, '%Y-%m-%d')


def pickle_object(python_obj, pickle_path):
    with open(pickle_path, 'wb') as f:
        pickle.dump(python_obj, f)
    return True


def load_pickle(pickle_path):
    with open(pickle_path, 'rb') as f:
        python_obj = pickle.load(f)
    return python_obj


def merge_two_dfs(list_of_dfs, common_col='Date'):
    assert len(list_of_dfs) == 2
    return pandas.merge(*list_of_dfs, on=common_col)


def merge_n_dfs(list_of_dfs, common_col):
    df1, df2 = list_of_dfs[0], list_of_dfs[1]
    merged = merge_two_dfs([df1, df2],
                           common_col=common_col)

    for df in list_of_dfs[2:]:
        merged = merge_two_dfs([merged, df],
                               common_col=common_col)

    return merged
