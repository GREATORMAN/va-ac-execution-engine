import numpy as np
import matplotlib.pyplot as plt

from src.data import get_data, estimate_volatility, estimate_impact
from src.model import almgren_chriss
from src.strategies import twap, volatility_adaptive_ac
from src.simulation import run_simulation
from src.stats import bootstrap_diff

# -----------------------
# LOAD DATA
# -----------------------
prices, returns = get_data("AAPL")

sigma = estimate_volatility(returns)
eta = estimate_impact(prices)

# SAFETY CHECKS
if not np.isfinite(sigma) or sigma <= 0:
    sigma = 0.02

if not np.isfinite(eta) or eta <= 0:
    eta = 0.01

print("Estimated Volatility:", sigma)
print("Estimated Impact:", eta)

# -----------------------
# PARAMETERS
# -----------------------
X = 100000
T = 1
N = 50
lam = 1e-6

# -----------------------
# STRATEGIES
# -----------------------
v_ac = almgren_chriss(X, T, N, sigma, eta, lam)
v_twap = twap(X, T, N)

# simulated price path for adaptive strategy
sim_prices = np.linspace(100, 102, N)
v_vaac = volatility_adaptive_ac(v_ac, sim_prices)

# -----------------------
# SIMULATION
# -----------------------
cost_ac = run_simulation(v_ac, sigma)
cost_twap = run_simulation(v_twap, sigma)
cost_vaac = run_simulation(v_vaac, sigma)

# REMOVE NaN / INF VALUES
cost_ac = cost_ac[np.isfinite(cost_ac)]
cost_twap = cost_twap[np.isfinite(cost_twap)]
cost_vaac = cost_vaac[np.isfinite(cost_vaac)]

# -----------------------
# RESULTS
# -----------------------
print("\n=== MEAN COSTS ===")

if len(cost_ac) > 0:
    print("AC:", np.mean(cost_ac))
else:
    print("AC: No valid data")

if len(cost_twap) > 0:
    print("TWAP:", np.mean(cost_twap))
else:
    print("TWAP: No valid data")

if len(cost_vaac) > 0:
    print("VA-AC:", np.mean(cost_vaac))
else:
    print("VA-AC: No valid data")

# -----------------------
# BOOTSTRAP VALIDATION
# -----------------------
if len(cost_ac) > 0 and len(cost_vaac) > 0:
    diffs = bootstrap_diff(cost_vaac, cost_ac)

    lower = np.percentile(diffs, 2.5)
    upper = np.percentile(diffs, 97.5)

    print("\nVA-AC vs AC 95% CI:", lower, upper)
else:
    print("\nBootstrap skipped (insufficient data)")

# -----------------------
# PLOT
# -----------------------
plt.figure()

if len(cost_ac) > 0:
    plt.hist(cost_ac, alpha=0.5, label="AC")

if len(cost_twap) > 0:
    plt.hist(cost_twap, alpha=0.5, label="TWAP")

if len(cost_vaac) > 0:
    plt.hist(cost_vaac, alpha=0.5, label="VA-AC")

plt.legend()
plt.title("Execution Cost Distribution")
plt.xlabel("Cost")
plt.ylabel("Frequency")

plt.show()