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
#  1. INTEGER m
#  2. INTEGER a
#

MOD = 1000000007

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

MAX = 100000 + 100000
P = [1] * (MAX + 1)
invP = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    t = i * (i + 1) // 2
    P[i] = (t * P[i - 1]) % MOD
    invP[i] = modinv(P[i], MOD)

def solve(m, a):
    return (P[m + a + 1] * invP[a + 1]) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d = int(input().strip())

    for d_itr in range(d):
        first_multiple_input = input().rstrip().split()

        m = int(first_multiple_input[0])

        a = int(first_multiple_input[1])

        result = solve(m, a)

        fptr.write(str(result) + '\n')

    fptr.close()
