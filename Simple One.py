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
#  1. INTEGER p
#  2. INTEGER q
#  3. INTEGER n
#

MOD = 1000000007

def mul(x, y):
    return ((x[0] * y[0] - x[1] * y[1]) % MOD, (x[0] * y[1] + x[1] * y[0]) % MOD)

def mpow(x, n):
    res = (1, 0)
    while n:
        if n & 1:
            res = mul(res, x)
        x = mul(x, x)
        n //= 2
    return res

def solve(p, q, n):
    tg = p * pow(q, MOD - 2, MOD) % MOD
    a = (1, tg)
    an = mpow(a, n)
    res = an[1] * pow(an[0], MOD - 2, MOD) % MOD
    return (res + MOD) % MOD


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = int(first_multiple_input[0])

        q = int(first_multiple_input[1])

        n = int(first_multiple_input[2])

        result = solve(p, q, n)

        fptr.write(str(result) + '\n')

    fptr.close()
