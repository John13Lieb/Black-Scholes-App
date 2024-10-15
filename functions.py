from math import exp, sqrt, log
from scipy.stats import norm

# calculates the intermediate values d1 and d2
def get_intermediates(S, K, sigma, r, T):
    d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    return d1, d2

# calculates the call and put option prices
def calc_prices(S, K, sigma, r, T):
    if S > 0 and K > 0 and sigma >= 0 and T > 0:
        d1, d2 = get_intermediates(S, K, sigma, r, T)
        call = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
        put = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        return call, put
    else:
        return None

# calculates the greeks of the option for a given option type
def calc_greeks(S, K, sigma, r, T, option_type):
    d1, d2 = get_intermediates(S, K, sigma, r, T)

    delta, theta, rho = 0, 0, 0
    gamma = norm.pdf(d1) / (S * sigma * sqrt(T))
    vega = S * norm.pdf(d1) * sqrt(T)

    if option_type == 'call':
        delta = norm.cdf(d1)
        theta = -S * norm.pdf(d1) * sigma / (2 * sqrt(T)) - r * K * exp(-r * T) * norm.cdf(d2)
        rho = K * T * exp(-r * T) * norm.cdf(d2)

    elif option_type == 'put':
        delta = norm.cdf(d1) - 1
        theta = -S * norm.pdf(d1) * sigma / (2 * sqrt(T)) + r * K * exp(-r * T) * norm.cdf(-d2)
        rho = -K * T * exp(-r * T) * norm.cdf(-d2)

    return delta, gamma, theta, vega, rho

# def put_call_parity(S, K, r, T, call, put):
#     return call - put - S + K * exp