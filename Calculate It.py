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
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING x
#

def hRank(n, k):
    n //= k  # Use integer division
    omni = [[[i, 1] for i in range(1, k + 1)]]
    bound = 1
    while k**bound <= n:
        bound += 1
        row = [0] * (bound) + [1]
        mat = [row.copy()]
        for i in range(k):
            for j in range(bound - 1):
                c = omni[-1][-1][j]
                for m in range(j + 2):
                    row[m] += c * omni[j][i][m]
            mat.append(row.copy())
        omni.append(mat)
    V = [1] + [0] * (bound)
    for i in range(bound, 0, -1):
        d, n = divmod(n, k**(i - 1))
        V = [sum(omni[j][d][m] * V[m] for m in range(j + 2)) for j in range(i)]
    return V[0]

k, x = map(int, input().split())
print(hRank(x, k))


