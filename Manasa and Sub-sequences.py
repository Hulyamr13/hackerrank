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
# The function accepts STRING s as parameter.
#

MOD = 1000000007


def powmod(x, k, MOD):
    p = 1
    if k == 0:
        return p
    if k == 1:
        return x
    while k != 0:
        if k % 2 == 1:
            p = (p * x) % MOD
        x = (x * x) % MOD
        k //= 2
    return p


def manasa(s):
    result = 0
    m = len(s) - 1
    q = 1

    for c in s[::-1]:
        c = int(c)
        p = powmod(2, m, MOD)
        x = (c * p) % MOD
        result = (result + x * q) % MOD
        m -= 1
        q = (q * 11) % MOD

    return result


def solve(s):
    return manasa(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(str(result) + '\n')

    fptr.close()
