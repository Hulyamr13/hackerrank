import math

n = int(input())
numbers = list(map(int, input().split()))
witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
Primes = []
IsPrime = [True] * 100001

for p in range(2, 100000):
    if not IsPrime[p]:
        continue
    Primes.append(p)
    mult = p * p
    while mult < 100001:
        IsPrime[mult] = False
        mult += p

def get_rid_of_2(n):
    while n % 2 == 0:
        n //= 2
    return n

def is_composite(n, a, s, d):
    if pow(a, d, n) == 1:
        return False
    for r in range(s):
        if pow(a, (1 << r) * d, n) == n - 1:
            return False
    return True

def is_prime(n):
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    for a in witnesses:
        if is_composite(n, a, s, d):
            return False
    return True

def is_n_power_of_prime(n):
    if is_prime(n):
        return True
    sqrt = int(math.sqrt(n))
    if sqrt * sqrt == n and is_prime(n):
        return True
    return False

def is_n_square(n):
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n

def factor(n):
    nb_factors = 0
    sum_factors = 0
    if n % 2 == 0:
        nb_factors += 1
        n = get_rid_of_2(n)
    if is_n_square(n):
        sum_factors = 1
        n = int(math.sqrt(n))
    for prime in Primes:
        if n == 1:
            break
        if n % prime != 0:
            continue
        nb_factors += 1
        n //= prime
        while n % prime == 0:
            n //= prime
    if n == 1:
        return nb_factors, sum_factors
    if is_n_power_of_prime(n):
        return nb_factors + 1, sum_factors
    return nb_factors + 2, sum_factors

result = [[0, 0], [0, 0]]
for num in numbers:
    nb, s = factor(num)
    result[nb % 2][s] += 1

final_result = max(
    result[0][0] + result[0][1],
    result[0][0] + result[1][0],
    result[1][1] + result[1][0],
    result[1][1] + result[0][1]
)
print(final_result)
