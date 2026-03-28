import numpy as np

def simulate_price(S0, sigma, N):
    prices = [S0]
    for _ in range(N-1):
        prices.append(prices[-1] + sigma * np.random.randn())
    return np.array(prices)

def nonlinear_impact(v, sigma, daily_volume=1e6):
    return sigma * np.sqrt(np.abs(v) / daily_volume)

def execution_cost(v, prices, sigma):
    cost = 0
    for i in range(len(v)):
        impact = nonlinear_impact(v[i], sigma)
        cost += v[i] * (prices[i] + impact)
    return cost

def run_simulation(v, sigma, runs=300):
    costs = []
    for _ in range(runs):
        prices = simulate_price(100, sigma, len(v)+1)
        costs.append(execution_cost(v, prices, sigma))
    return np.array(costs)