from math import comb

def binomial_probability(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def no_more_than_2_rejects_probability():
    total_pistons = 10
    reject_probability = 0.12
    probability_no_more_than_2_rejects = sum(
        binomial_probability(total_pistons, k, reject_probability) for k in range(3)
    )
    return round(probability_no_more_than_2_rejects, 3)

def at_least_2_rejects_probability():
    total_pistons = 10
    reject_probability = 0.12
    probability_at_least_2_rejects = sum(
        binomial_probability(total_pistons, k, reject_probability) for k in range(2, total_pistons + 1)
    )
    return round(probability_at_least_2_rejects, 3)

result_a = no_more_than_2_rejects_probability()
result_b = at_least_2_rejects_probability()

print(result_a)
print(result_b)
