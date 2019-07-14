import yfinance as yf

gs = yf.Ticker("GS")

hist = gs.history(period="max")


if __name__ == "__main__":
    pass
