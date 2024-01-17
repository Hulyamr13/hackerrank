#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highwayConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. INTEGER k
#

MOD = 10 ** 9 + 9

B = [0 for _ in range(1001)]
inv = [i for i in range(10001)]
fac = [i for i in range(10001)]
fac[0] = 1

for i in range(1, 10001):
    inv[i] = pow(i, MOD - 2, MOD)

for i in range(1, 10001):
    fac[i] = fac[i - 1] * i
    fac[i] %= MOD

invfac = fac[:]
for i in range(len(invfac)):
    invfac[i] = pow(invfac[i], MOD - 2, MOD)

def comb(n, k):
    return fac[n] * invfac[n - k] * invfac[k] % MOD

B[0] = 1
B[1] = (MOD - 1) * pow(2, MOD - 2, MOD) % MOD

for m in range(2, 1001):
    for k in range(m):
        B[m] -= comb(m, k) * B[k] * inv[m - k + 1] % MOD
        B[m] %= MOD

B[1] = MOD - B[1]

def f(n, p):
    res = 0
    for k in range(p + 1):
        res += comb(p, k) * B[p - k] * pow(n, k + 1, MOD) * inv[k + 1] % MOD
        res %= MOD
    return res

def highwayConstruction(n, k):
    if n <= 2:
        return 0
    return (f(n - 1, k) + MOD - 1) % MOD

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, k = map(int, input().strip().split())
        result = highwayConstruction(n, k)
        print(result)

