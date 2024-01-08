
#!/bin/python3

import sys

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(limit + 1) if primes[i]]


def nth_prime_number(n):
    primes = sieve_of_eratosthenes(110000)
    return primes[n - 1]


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        result = nth_prime_number(n)
        print(result)
