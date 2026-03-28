import numpy as np

def twap(X, T, N):
    return np.ones(N-1) * (X / T)

def rolling_volatility(prices, window=5):
    returns = np.diff(np.log(prices))
    vol = np.zeros(len(prices))
    
    for i in range(window, len(returns)):
        vol[i] = np.std(returns[i-window:i])
        
    return vol

def volatility_adaptive_ac(v_ac, prices, alpha=5):
    vol = rolling_volatility(prices)
    
    adjusted = []
    for i in range(len(v_ac)):
        factor = 1 + alpha * vol[i]
        adjusted.append(v_ac[i] * factor)
    
    return np.array(adjusted)