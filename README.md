# Volatility-Adaptive Optimal Execution Engine

A quantitative finance project implementing and extending the Almgren–Chriss optimal execution model for trade execution under market impact and uncertainty.

---

## 📌 Overview

This project simulates optimal execution strategies for large trades in financial markets. It incorporates stochastic price dynamics, market impact modeling, and statistical validation to evaluate execution performance.

---

## ⚙️ Features

- Almgren–Chriss optimal execution model  
- Volatility-Adaptive execution strategy (VA-AC)  
- Nonlinear market impact (square-root law)  
- Monte Carlo price simulation  
- Bootstrap-based statistical validation  
- Strategy comparison (AC vs TWAP vs VA-AC)

---

## 📊 Methodology

1. **Data Calibration**
   - Estimated volatility from real market data (Yahoo Finance)
   - Approximated market impact from price changes

2. **Execution Strategies**
   - Baseline: TWAP (Time-Weighted Average Price)
   - Optimal: Almgren–Chriss model
   - Extension: Volatility-Adaptive AC (VA-AC)

3. **Simulation**
   - Generated stochastic price paths
   - Evaluated execution cost across multiple simulations

4. **Validation**
   - Compared cost distributions
   - Used bootstrap sampling to assess statistical significance

---

## 📈 Results

- TWAP performed competitively under current assumptions  
- The volatility-adaptive strategy did not consistently outperform the baseline model  
- Results suggest that **market impact dominates short-term volatility** in execution optimization  

---

## 🧠 Key Insight

> Simple volatility-based adjustments are insufficient to improve execution performance without accounting for dominant market impact effects.

---

## 🛠️ Tech Stack

- Python  
- NumPy  
- Matplotlib  
- SciPy  
- yfinance  

---

## ▶️ How to Run

```bash
python main.py
