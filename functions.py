from math import exp, sqrt, log
from scipy.stats import norm

# calculates the call option price
def call_price(S, K, sigma, r, T):
    if S > 0 and K > 0 and sigma >= 0 and T > 0:
        d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
        d2 = d1 - sigma * sqrt(T)
        call = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
        return call
    else:
        return None

# calculates the put option price
def put_price(S, K, sigma, r, T):
    if S > 0 and K > 0 and sigma >= 0 and T > 0:
        d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
        d2 = d1 - sigma * sqrt(T)
        put = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        return put
    else:
        return None