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
#  1. INTEGER a
#  2. LONG_INTEGER n
#  3. INTEGER m
#

def powMod(a, n, mod):
    res = 1
    while n:
        if n % 2:
            res = (res * a) % mod
        n //= 2
        a = (a * a) % mod
    return res % mod

def myPow(a, n):
    res = 1
    while n:
        if n % 2:
            res *= a
        n //= 2
        a *= a
    return res


def solve(a, n, m):
    def solve_recursive(n, x, m):
        if n == 0:
            return 1
        if n == 1:
            return (powMod(10, x, m) + 1) % m
        res = 1
        log2 = int(math.log2(n))
        for i in range(log2):
            res = (res * (1 + powMod(powMod(10, x, m), myPow(2, i), m))) % m
        y = myPow(2, log2)
        return (res + ((powMod(powMod(10, x, m), y, m) * solve_recursive(n - y, x, m)) % m)) % m

    return solve_recursive(n - 1, len(str(a)), m) * a % m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        a, n, m = map(int, input().split())
        result = solve(a, n, m)
        fptr.write(str(result) + '\n')

    fptr.close()

