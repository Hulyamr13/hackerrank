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
# The function accepts INTEGER n as parameter.
#

def digit_sum(x):
    return sum(int(d) for d in str(x))


def prime_factor_sum(x):
    factors = []
    while x % 2 == 0:
        factors.append('2')
        x //= 2

    p = 3
    while p * p <= x:
        while x % p == 0:
            factors.append(str(p))
            x //= p
        p += 2

    if x > 2:
        factors.append(str(x))

    return ''.join(factors)


if __name__ == "__main__":
    n = int(input())

    if n == 1:
        print(0)
    else:
        ds = digit_sum(n)
        pfs = digit_sum(prime_factor_sum(n))
        print(1 if ds == pfs else 0)

