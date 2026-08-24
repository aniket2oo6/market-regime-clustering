import yfinance as yf
import pandas as pd

def load_data(ticker):
    df = yf.download(ticker, start = "1993-01-01")
    df.columns = df.columns.get_level_values(0)
    df["Return"] = df["Close"].pct_change()
    df["Volatility"] = df["Return"].rolling(window = 21).std()
    df = df.dropna()
    return df

