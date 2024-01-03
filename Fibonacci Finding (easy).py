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
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER n
#

MOD = 10 ** 9 + 7


class Matrix:
    def __init__(self, q, w, e, r):
        self.a = q
        self.b = w
        self.c = e
        self.d = r


def matrix_multiply(A, B):
    C = Matrix(0, 0, 0, 0)
    C.a = (A.a * B.a + A.b * B.c) % MOD
    C.b = (A.a * B.b + A.b * B.d) % MOD
    C.c = (A.c * B.a + A.d * B.c) % MOD
    C.d = (A.c * B.b + A.d * B.d) % MOD
    return C


def power(M, n):
    if n == 1:
        return M
    res = power(M, n // 2)
    res = matrix_multiply(res, res)
    if n % 2 == 1:
        res = matrix_multiply(res, M)
    return res


def solve(a, b, n):
    if n == 1:
        return b
    n -= 1
    M = Matrix(1, 1, 1, 0)
    res = power(M, n)
    return (res.a * b + res.b * a) % MOD


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        n = int(first_multiple_input[2])

        result = solve(a, b, n)

        fptr.write(str(result) + '\n')

    fptr.close()
