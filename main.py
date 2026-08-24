from data import load_data
from clustering import fit_gmm, label
from visual import plot_regimes

stock = load_data("AAPL")
stock, gmm = fit_gmm(stock)
stock = label(stock)

#plot_regimes(spy)

print(stock[["Close", "Regime", "Regime_Label"]].tail(10))

