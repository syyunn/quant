import matplotlib.pyplot as plt
from Data import Data, get_technical_indicators


def plot_technical_indicators(dataset,
                              last_days):
    ticker = dataset.columns.values[1]
    plt.figure(figsize=(16, 10), dpi=100)
    shape_0 = dataset.shape[0]
    xmacd_ = shape_0 - last_days

    dataset = dataset.iloc[-last_days:, :]
    x_ = range(3, dataset.shape[0])
    x_ = list(dataset.index)

    # Plot first subplot
    plt.subplot(2, 1, 1)
    plt.plot(dataset['ma7'], label='MA 7', color='g', linestyle='--')
    plt.plot(dataset[ticker], label='Closing Price', color='b')
    plt.plot(dataset['ma21'], label='MA 21', color='r', linestyle='--')
    plt.plot(dataset['upper_band'], label='Upper Band', color='c')
    plt.plot(dataset['lower_band'], label='Lower Band', color='c')
    plt.fill_between(x_, dataset['lower_band'], dataset['upper_band'],
                     alpha=0.35)
    plt.title('Technical indicators for Goldman Sachs - last {} days.'.format(
        last_days))
    plt.ylabel('USD')
    plt.legend()

    # Plot second subplot
    plt.subplot(2, 1, 2)
    plt.title('MACD')
    plt.plot(dataset['MACD'], label='MACD', linestyle='-.')
    plt.hlines(15, xmacd_, shape_0, colors='g', linestyles='--')
    plt.hlines(-15, xmacd_, shape_0, colors='g', linestyles='--')
    plt.plot(dataset['log_momentum'], label='Momentum', color='b',
             linestyle='-')
    plt.savefig(
        '../assets/Techinical_indicators_for_Goldman_Sachs_last_400_days.png')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    data = Data('GS')
    df = data.get_close_data()

    df_ti = get_technical_indicators(df)

    plot_technical_indicators(df_ti, 400)
