import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start="2020-01-01", end="2023-01-01"):
    df = yf.download(ticker, start=start, end=end)
    return df

if __name__ == "__main__":
    data = fetch_stock_data("AAPL")
    print(data.head())
