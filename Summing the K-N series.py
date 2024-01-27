#!/bin/python3

import math
import os
import random
import re
import sys

P = 10**9 + 7

def power_mod(n, k):
    r = 1
    while k > 0:
        if k & 1:
            r *= n
            r %= P
        n *= n
        n %= P
        k >>= 1
    return r

def S(N, K):
    c = [1]
    inv = [0, 1]
    s = []
    for k in range(1, K + 1):
        # n*(p/n)*inv[p%n]
        inv.append(P - (P // (k + 1)) * inv[P % (k + 1)] % P)
    for k in range(K + 1):
        c = [x + y for x, y in zip([0] + c, c + [0])]
        r = power_mod(N + 1, k + 1) - 1
        if r < 0:
            r += P
        for i in range(k):
            r -= c[i] * s[i] % P
            if r < 0:
                r += P
        r *= inv[k + 1]
        r %= P
        s.append(r)
    return s[K]

def solve(n, k):
    return S(n, k)


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
