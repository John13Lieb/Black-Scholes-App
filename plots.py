import numpy as np
import plotly.graph_objects as go
from functions import calc_prices, calc_pnl

# generates spot prices and volatilities
def generate_spot_and_vol(S_min, S_max, sigma_min, sigma_max):
    spot_prices = np.linspace(S_min, S_max, 10)
    volatilities = np.linspace(sigma_min, sigma_max, 10)
    return spot_prices, volatilities

# populates PnL call and put matrices for each combination of spot price and volatility
def populate_pnl_matrices(S, K, sigma, r, T, spot_prices, volatilities, purchase_price):
    call_matrix = np.zeros((10, 10))
    put_matrix = np.zeros((10, 10))

    for i, sigma in enumerate(volatilities):
        for j, S in enumerate(spot_prices):
            call_price, put_price = calc_prices(S, K, sigma, r, T)
            call_matrix[i, j] = calc_pnl(purchase_price, call_price)
            put_matrix[i, j] = calc_pnl(purchase_price, put_price)

    return call_matrix, put_matrix