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
#  2. INTEGER m
#

MOD = 1000000007

def mod_exp(a, b, n):
    c = 1
    d = a
    while b:
        if b & 1:
            c = (c * d) % n
        d = (d * d) % n
        b >>= 1
    return c

def solve(n, m):
    isprime = [True] * 15000001
    isprime[0] = isprime[1] = False
    factor = []

    nf = 0
    for i in range(2, min(n, m) + 1):
        if isprime[i]:
            for j in range(i + i, min(n, m) + 1, i):
                isprime[j] = False
            factor.append(i)
            nf += 1

    ans = 1

    for i in range(nf):
        tmp = 0
        now = factor[i]
        while n // now and m // now:
            tmp += (n // now) * (m // now)
            now *= factor[i]
        ans = (ans * mod_exp(factor[i], tmp, MOD)) % MOD

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
