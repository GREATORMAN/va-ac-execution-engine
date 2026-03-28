import yfinance as yf
import numpy as np

def get_data(ticker="AAPL"):
    data = yf.download(ticker, period="6mo", interval="1d")
    prices = data['Close'].dropna().values
    returns = np.diff(np.log(prices))
    return prices, returns

def estimate_volatility(returns):
    return np.std(returns)

def estimate_impact(prices):
    returns = np.diff(prices)
    return np.mean(np.abs(returns))