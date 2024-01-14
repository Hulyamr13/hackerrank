from math import comb

def binomial_probability(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def at_least_3_boys_probability():
    total_children = 6
    boys_ratio = 1.09 / (1 + 1.09)
    probability_at_least_3_boys = sum(
        binomial_probability(total_children, k, boys_ratio) for k in range(3, total_children + 1)
    )
    return round(probability_at_least_3_boys, 3)

result = at_least_3_boys_probability()
print(result)
