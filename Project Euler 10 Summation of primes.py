#!/bin/python3

def generate_primes_up_to_limit(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return primes

def generate_sum_of_primes(primes):
    n = len(primes)
    prime_sum = [0] * n

    for i in range(1, n):
        prime_sum[i] = prime_sum[i - 1] + (i if primes[i] else 0)

    return prime_sum


N = 1000001
primes = generate_primes_up_to_limit(N)
prime_sum = generate_sum_of_primes(primes)

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(prime_sum[n])
