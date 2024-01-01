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
#  1. INTEGER d
#  2. 2D_INTEGER_ARRAY points
#

MOD = 1000000009

def calculate_ss(X, d):
    ss = 0
    for k in range(d):
        sorted_X = sorted(X, key=lambda x: x[k + 1])
        HX = list(zip(*sorted_X))
        hjxj = 0
        hj = 0
        h = HX[0]
        x = HX[k + 1]
        for i in range(len(X) - 2, -1, -1):
            hj += h[i + 1]
            hjxj += h[i + 1] * x[i + 1]
            ss = (ss + h[i] * hjxj - h[i] * x[i] * hj) % MOD
    return ss

if __name__ == "__main__":
    n, d = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(n)]

    result = calculate_ss(X, d)
    print(result)
