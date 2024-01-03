# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def density(t):
    return math.exp(-t * t / 2) / math.sqrt(2 * math.pi)

def phi(t):
    tabs = abs(t)
    delta, eps = 0.001, 1e-6
    s = 0
    while True:
        d = delta * density(tabs)
        s += d
        tabs += delta
        if d < eps:
            break
    return s if t <= 0 else 1 - s

def normalize(mu, sigma):
    return lambda t: (t - mu) / sigma


n = normalize(30, 4)

print(phi(n(40)))
print(1 - phi(n(21)))
print(phi(n(35)) - phi(n(30)))
