def get_moving_averages(price_data, n_days):
    n_days = 3
    cumsum, moving_aves = [0], []
    for i, x in enumerate(price_data, 1):
        cumsum.append(cumsum[i-1] + x)
        if i >= n_days:
            moving_ave = (cumsum[i] - cumsum[i - n_days]) / n_days
            moving_aves.append(moving_ave)
    return moving_aves


if __name__ == "__main__":


    pass


