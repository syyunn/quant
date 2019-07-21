import quandl
import pandas as pd

from utils import parser
from Constants import sg_start


def get_libor():
    df = quandl.get("FRED/USDONTD156N", authtoken="UHqpEq3-QGzP5zTUSEYr")
    dates = list(df.index)
    interest_rates = list(df.values)

    parsed_dates = []
    rates = []
    for date, rate in zip(dates, interest_rates):
        date = parser(date._date_repr)
        parsed_dates.append(date)
        rate = rate[0]
        rates.append(rate)

    data_dict = {'Date': parsed_dates, 'LIBOR': rates}

    df = pd.DataFrame(data_dict)
    return df


if __name__ == "__main__":
    get_libor()
    pass
