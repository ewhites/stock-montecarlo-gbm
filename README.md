# Stock Price Simulation and Risk Analysis in Python

---

Hi, I'm Ethan — a senior-level physics and maths student at Tennessee Tech University. This project explores how physical models, like geometric brownian motion (GBM), can be applied to simulate stock price behavior and measure financial risk. A Monte Carlo analysis can be applied to this model to explore thousands of different price paths over time to probe valuable risk metrics liek Value at Risk (VaR) and probability of loss. Along the way, it demonstrates basic techniques used in real-world quantitative research and trading.

---

## What This Project Does

* Simulates a single or multiple GBM stock price paths
* Plots them over time
* Demonstrates how volatility and drift affect long-term outcomes

This forms the base for more complex models like Monte Carlo simulations for portfolios, option pricing, or risk modeling, which are discussed later on.

---

## What is Geometric Brownian Motion?

GBM is a stochastic process widely used to model the behavior of stock prices over time. It assumes:

* Constant drift (average return)
* Constant volatility
* Log-normal distribution of prices

It’s a core assumption behind models like Black-Scholes, and a building block in Monte Carlo simulations.

---

## How Geometric Brownian Motion Works

At its core, GBM assumes that stock prices grow continuously over time, but with some randomness. We use a formula that captures both the average growth (drift) and the randomness (volatility).

Here’s the equation we use to simulate it:

$$
S_{t+1} = S_t \cdot \exp\left( \left( \mu - \frac{1}{2} \sigma^2 \right) \Delta t + \sigma \sqrt{\Delta t} \cdot x_t \right)
$$

where:

* $S_t$: The stock price at time $t$
* $\mu$: The average return (drift)
* $\sigma$: The volatility (how much it varies)
* $\Delta t$: A small time step (like 1/252 for daily steps)
* $Z_t$: A random value drawn from a standard normal distribution (mean 0, standard deviation 1). 

This formula basically says: take the current price, and adjust it using both the average return and some randomness. That’s what gives the simulated path its wiggly, realistic shape. It’s powerful because it captures the idea that while we can expect growth over time, prices also bounce around in unpredictable ways.

---

## What Is A Monte Carlo Simulation?

A Monte Carlo simulation models uncertainty by running the same process (like GBM) many times using random inputs. In finance, this helps us:

- Visualize a range of possible outcomes
- Estimate the probability of gains or losses
- Measure risk under extreme market conditions

This framework supports scaling to thousands of simulations which you can see below.

---
## How It Works (Python)

Basic Parameters for SPY, as of Sept 7th, 2025:

```python
price = 647.24    # initial stock price
mu = 0.10         # expected anunual return
sigma = 0.1125    # annual volatility
y = 1             # time in years
n = 252           # number of steps
dt = y/n          # step size
p = 10000         # number of simulation paths
```

Simulation:
```python
# sSet up array for all paths
paths = np.zeros((p, n+1))
paths[:, 0] = price   # initialize all paths at our initial price

# Generate all random shocks (x) at once
x = np.random.normal(0, 1, size=(p, n))

# simulate paths
for t in range(1, n+1):
    price_paths[:, t] = price_paths[:, t-1] * np.exp(
        (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * x[:, t-1]
    )
```

You can check out the full simulation code [here](https://github.com/ewhites/stock-montecarlo-gbm/blob/main/gbm_montecarlo.py)

---
## Example Output

![Portfolio Simulation Output](https://github.com/ewhites/stock-montecarlo-gbm/blob/main/simulation.png)

## Visualizing Risk: Histogram + Path Plot

To analyze the risk in a meaningful way, we can:

- Plot multiple simulated price paths
- Create a histogram of the final prices across all simulations

This lets us estimate downside risk with:

- Value at Risk (VaR) – the worst expected loss at a confidence level
- Probability of Loss – the probability of the stock having returns below the value you entered at

---

## Skills Demonstrated

This model demonstrates:

* Stochastic modeling (GBM)
* Portfolio-level Monte Carlo simulation
* Vectorized, production-style code
* Risk analysis (VaR, probability of loss)

---

## Questions?

If you have any questions, feel free to email me through my contacts on [my website!](ewhites.github.io)

---

## Resources I Used

* [GBM Article: Quant Start](https://www.quantstart.com/articles/geometric-brownian-motion-simulation-with-python/)
