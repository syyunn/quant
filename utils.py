import datetime
import pickle


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
