#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

from math import isqrt, gcd


def is_even_perfect_square(n):
    return (n % 2 == 0) and (isqrt(n) ** 2 == n)


def solve(n):
    cd = 1
    cepsd = 0
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            cd += 1
            if is_even_perfect_square(d):
                cepsd += 1
            dd = n // d
            if dd == d:
                continue
            cd += 1
            if is_even_perfect_square(dd):
                cepsd += 1

    if not cepsd:
        return "0"

    res = f"{cepsd // gcd(cepsd, cd)}/{cd // gcd(cepsd, cd)}"
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
