from plots.Techinical_indicators_for_Goldman_Sachs_last_400_days \
    import get_technical_indicators

from Data import Data


def get_feature_importance_data(ticker,
                                data_income):
    data = data_income.copy()
    y = data[ticker]
    X = data.iloc[:, 1:]

    train_samples = int(X.shape[0] * 0.65)

    X_train = X.iloc[:train_samples]
    X_test = X.iloc[train_samples:]

    y_train = y.iloc[:train_samples]
    y_test = y.iloc[train_samples:]

    return (X_train, y_train), (X_test, y_test)


ticker = 'GS'
data = Data(ticker)
df = data.get_close_data()

df_ti = get_technical_indicators(df)


# Get training and test data
(X_train_FI, y_train_FI), (X_test_FI, y_test_FI) = \
    get_feature_importance_data(ticker, df_ti)

if __name__ == "__main__":
    pass
