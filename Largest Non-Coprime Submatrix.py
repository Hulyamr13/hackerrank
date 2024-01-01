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
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def gcd(u, v):
    while v != 0:
        r = u % v
        u = v
        v = r
    return u


def max_submatrix(matrix, n, m):
    r = 0

    for x1 in range(n):
        for y1 in range(m):
            if r > (n - x1) * (m - y1):
                break

            sub_gcd = [0] * m

            for x2 in range(x1, n):
                g = 0
                for y2 in range(y1, m):
                    g = gcd(gcd(g, matrix[x2][y2]), sub_gcd[y2])
                    sub_gcd[y2] = g

                    if g == 1:
                        break

                    r = max(r, (x2 - x1 + 1) * (y2 - y1 + 1))
    return r


def solve(matrix):
    n = len(matrix)
    m = len(matrix[0])

    return max_submatrix(matrix, n, m)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = solve(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
