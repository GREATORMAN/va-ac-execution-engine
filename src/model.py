import numpy as np

def almgren_chriss(X, T, N, sigma, eta, lam):
    dt = T / N
    t = np.linspace(0, T, N)

    # SAFETY FIXES
    sigma = max(sigma, 1e-6)
    eta = max(eta, 1e-6)
    lam = max(lam, 1e-10)

    kappa = np.sqrt((lam * sigma**2) / eta)

    # avoid division by zero in sinh
    denom = np.sinh(kappa * T)
    if denom == 0:
        denom = 1e-6

    x = X * np.sinh(kappa * (T - t)) / denom

    v = -np.diff(x) / dt

    return v