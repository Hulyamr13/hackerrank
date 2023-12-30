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

def S_brutforce(n):
    s = 0
    i = 0
    while 2 ** i <= n:
        for j in range(0, n + 1):
            s += 2 ** (2 ** i + 2 * j)
        i += 1
    return s


def S(n):
    i = n
    k = 0
    while i != 0:
        i //= 2
        k += 1
    if k == 1:
        s1 = 2
    else:
        s1 = [6, 2, 8, 4, 0][(k - 2) % 5]

    s2 = 1 if n % 2 == 0 else 5

    return (s1 * s2) % 10


def solve(n):
    if n % 2 == 1:
        return 0
    else:
        s = S(n)
        return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()
