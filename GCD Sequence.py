#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

MOD = 10 ** 9 + 7

def prime_sieve(n):
    A = [0, 0] + [1 for _ in range(n - 1)]
    sqrt_n = int(n ** 0.5)
    for i in range(2, sqrt_n + 1):
        if A[i] == 1:
            for j in range(i * i, n + 1, i):
                A[j] = 0
    return [i for i, prime in enumerate(A) if prime]

def moebius_sieve(N):
    P = prime_sieve(N + 1)
    Mu = [1] * (N + 1)
    Mu[0] = 0
    for p in P:
        for q in range(p, N + 1, p):
            Mu[q] *= -1
        for q in range(p * p, N + 1, p * p):
            Mu[q] = 0
    return Mu

def fact_and_inv_fact_tables(n, m):
    fact, inv_fact = [1] + n * [0], [1] + n * [0]
    for k in range(1, n + 1):
        fact[k] = fact[k - 1] * k % m
    inv_fact[n] = pow(fact[n], m - 2, m)
    for k in range(n, 1, -1): inv_fact[k - 1] = inv_fact[k] * k % m
    return fact, inv_fact

def solve(n, k):
    mu = moebius_sieve(10 ** 5)
    s = 0
    fact, inv_fact = fact_and_inv_fact_tables(n + k, MOD)
    for i in range(1, n + 1):
        s = (s + mu[i] * (fact[n // i + k - 1] * inv_fact[k] * inv_fact[n // i - 1]) % MOD) % MOD
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = solve(n, k)

        fptr.write(str(result) + '\n')

    fptr.close()

