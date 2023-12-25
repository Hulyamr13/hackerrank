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
#  2. INTEGER r
#  3. INTEGER m
#

def binomial_coefficient(n, k):
    if n < k:
        return 0
    ans = 1
    k = min(k, n - k)
    for i in range(1, k + 1):
        if n % i == 0:
            ans *= n // i
        elif ans % i == 0:
            ans = (ans // i) * n
        else:
            ans = (ans * n) // i
        n -= 1
    return ans

def lucas_theorem(n, k, p):
    ans = 1
    while k > 0:
        tmp_n = n % p
        tmp_k = k % p
        ans *= binomial_coefficient(tmp_n, tmp_k) % p
        ans %= p
        n //= p
        k //= p
    return ans

def get_remainder_squarefree(n, k, m):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    ans = -1
    last = 1

    if m == 1:
        return 0

    for prime in primes:
        if m % prime != 0:
            continue

        rem = lucas_theorem(n, k, prime)

        if ans == -1:
            ans = rem
        else:
            for j in range(50):
                if (ans + (last * j)) % prime == rem:
                    ans = ans + (last * j)
                    break
        last *= prime
        m //= prime

    return ans


def solve(n, r, m):
    return get_remainder_squarefree(n, r, m)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = solve(n, r, m)

        fptr.write(str(result) + '\n')

    fptr.close()
