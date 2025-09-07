import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import yfinance as yf

def stockprice():
    data = yf.download("SPY", period="1d", progress=False)
    if data.empty:
        print("Empty dataframe from yfinance. Using fallback price.")
        price = 647.24  # fallback value if yfinance has too many requests
    if not data.empty: price = float(data["Close"].iloc[-1])
    return price

def parameters(): # adjust based on stock ticker! currently set for SPY.
    mu = 0.10                # expected annual return
    sigma = 0.1125           # annual volatility
    y = 1                    # time in years
    n = 252                  # number of steps (trading days)  
    dt = y / n               # time step size
    p = 10000                # number of simulation paths
    return mu, sigma, y, n, dt, p

def montecarlo(p, n, price, mu, sigma, dt):
    price_paths = np.zeros((p, n+1))
    price_paths[:, 0] = price

    x = np.random.normal(0, 1, size=(p, n))
    for t in range(1, n+1):
        price_paths[:, t] = price_paths[:, t-1] * np.exp(             # closed-form SDE of GBM
        (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * x[:, t-1]) # monte-carlo volatility implementation
        
    price_final = price_paths[:, -1]  # shapes the array
    return price_paths, price_final

def plot(paths, final, price):
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    # plotting the 50 first paths of pricing
    for i in range(250): axs[0].plot(paths[i], lw=1.2, alpha=0.7)
    axs[0].set_title("250 Monte Carlo Simulated Price Paths")
    axs[0].set_xlabel("Trading Days [d]")
    axs[0].set_ylabel("Price [$]")

    # histogram of final prices
    axs[1].hist(final, bins=100, edgecolor='black')
    axs[1].set_title("Distribution of Final Simulated Prices (1 Year)")
    axs[1].set_xlabel("Final Price [$]")
    axs[1].set_ylabel("Frequency [#]")

    # risk metrics
    mean_price = np.mean(final)
    var_5 = np.percentile(final, 5)
    prob_loss = np.mean(final < price)

    # vertical lines for easier visiblity
    axs[0].axhline(price, color='black',linestyle='--',label=f'Initial Price')  
    axs[1].axvline(var_5, color='orange', linestyle='--', label=f'VaR (5%)')
    axs[1].axvline(mean_price, color='red', linestyle='--', label=f'Mean Price')
    axs[1].axvline(price, color='black', linestyle='--', label=f'Initial Price')

    axs[0].legend(facecolor='wheat',edgecolor='gray',loc='upper right')
    axs[1].legend(facecolor='wheat',edgecolor='gray',loc='upper left')  

    risk_text = (
        f"Mean Final Price: ${mean_price:.2f}\n"
        f"5% VaR: ${var_5:.2f} (loss: {price-var_5:.2f})\n"
        f"Probability of Loss: {prob_loss:.2%}"
    )

    axs[1].text(
        0.975, 0.975, risk_text,
        transform=axs[1].transAxes,
        fontsize=12,
        verticalalignment='top',
        horizontalalignment='right',
        bbox=dict(boxstyle="round,pad=0.4", facecolor='wheat', edgecolor='gray')
    )

    plt.grid(False)
    plt.tight_layout()
    plt.show()
    return

price = float(stockprice())
mu, sigma, y, n, dt, p = parameters()
paths, final = montecarlo(p, n, price, mu, sigma, dt)
plot(paths, final, price)
