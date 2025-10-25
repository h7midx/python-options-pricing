import math
def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))
def bs_price(S: float, K: float, r: float, sigma: float, T: float,
             option_type: str = "call", q: float = 0.0) -> float:
    if S <= 0 or K <= 0 or sigma <= 0 or T <= 0:
        raise ValueError("S, K, sigma, et T doivent être positifs.")
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    if option_type.lower() == "call":
        price = S * math.exp(-q * T) * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    elif option_type.lower() == "put":
        price = K * math.exp(-r * T) * norm_cdf(-d2) - S * math.exp(-q * T) * norm_cdf(-d1)
    else:
        raise ValueError("le type de l'option doit être 'call' ou 'put'.")
    return price
if __name__ == "__main__":
    S = 100
    K = 105
    r = 0.05
    sigma = 0.15
    T = 2.0
    call = bs_price(S, K, r, sigma, T, option_type="call")
    put = bs_price(S, K, r, sigma, T, option_type="put")
    print(f"Prix du call européen (BSM): {call:.4f}")
    print(f"Prix du put européen (BSM):  {put:.4f}")
