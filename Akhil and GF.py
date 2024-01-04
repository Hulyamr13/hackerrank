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
#  1. LONG_INTEGER n
#  2. INTEGER m
#

def mod_mul(x, y, n):
    if x == 0:
        return 0
    return (((x & 1) * y) % n + (mod_mul(x >> 1, y, n) << 1) % n) % n


def ModExp(b, n):
    c, d = 1, 10
    while b:
        if b & 1:
            c = mod_mul(c, d, n)
        d = mod_mul(d, d, n)
        b >>= 1
    return c


def solve(n, m):
    tmp = ModExp(n, 9 * m)
    tmp -= 1
    if tmp < 0:
        tmp += 9 * m
    return tmp // 9


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
