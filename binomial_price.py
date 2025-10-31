import math
def binomial_price(S, K, r, sigma, T, steps=100, option_type='call', q=0.0):
    dt = T / steps
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    disc = math.exp(-r * dt)
    p = (math.exp((r - q) * dt) - d) / (u - d)
    values = []
    for i in range(steps + 1):
        S_T = S * (u ** i) * (d ** (steps - i))
        if option_type == 'call':
            payoff = max(0, S_T - K)
        else:
            payoff = max(0, K - S_T)
        values.append(payoff)
    for step in range(steps - 1, -1, -1):
        for i in range(step + 1):
            values[i] = disc * (p * values[i + 1] + (1 - p) * values[i])

    return values[0]
