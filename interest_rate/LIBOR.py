import quandl


def get_libor():
    return quandl.get("FRED/USDONTD156N", authtoken="UHqpEq3-QGzP5zTUSEYr")


if __name__ == "__main__":
    pass
