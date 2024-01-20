from math import sqrt, erf

def CDF(x):
    return 0.5 * (1 + erf((x - 70) / (sqrt(2) * 10)))

a = 100 * (1 - CDF(80))
b = 100 * (1 - CDF(60))
c = 100 * (CDF(60))

print(f"{a:.2f}")
print(f"{b:.2f}")
print(f"{c:.2f}")
