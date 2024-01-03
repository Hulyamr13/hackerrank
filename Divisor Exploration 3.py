#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisorExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER a
#  3. INTEGER d
#

MOD = 1000000007
PRIME_1000 = 7919
primes = []
sieve = [True] * (1 + PRIME_1000)
for n in range(2, PRIME_1000 + 1):
    if sieve[n]:
        primes.append(n)
        for i in range(n, PRIME_1000 + 1, n):
            sieve[i] = False


def binomial(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = 1
    den = 1
    for i in range(1, min(k, n - k) + 1):
        num *= (n + 1 - i)
        den *= i
    c = num // den
    return c


def f(i, p, a):
    num = p ** a
    for j in range(2, i + 1):
        num = p * num - binomial(a + j - 2, j - 2)
        num //= p - 1

    return num % MOD


def egcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def modinv(a, m):
    g, x, _ = egcd(a, m)
    assert g == 1
    return x % m


def fast_f(i, p, a):
    num, den = pow(p, a, MOD), 1
    c_num, c_den = 1, 1
    for j in range(2, i + 1):
        if j > 2:
            c_num = (c_num * (a + j - 2)) % MOD
            c_den = (c_den * (j - 2)) % MOD
        num = (p * num * c_den - c_num * den) % MOD
        den = (den * (p - 1) * c_den) % MOD

    num = (num * modinv(den, MOD)) % MOD

    return num


def solve(m, a, d):
    res = 1
    for i in range(m):
        x = fast_f(d, primes[i], a + i + 1) % MOD
        res *= x
        res %= MOD

    return res


def divisorExploration(m, a, d):
    return solve(m, a, d)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        m = int(first_multiple_input[0])

        a = int(first_multiple_input[1])

        d = int(first_multiple_input[2])

        result = divisorExploration(m, a, d)

        fptr.write(str(result) + '\n')

    fptr.close()
