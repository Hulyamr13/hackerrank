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
#  1. INTEGER r1
#  2. INTEGER r2
#  3. INTEGER_ARRAY position
#  4. INTEGER_ARRAY acceleration
#

def are_spheres_touching(R1, R2, P1, A1, P2, A2):
    eps = 0.00001

    def norm2(x):
        return sum(i * i for i in x) ** 0.5

    def add(x, y):
        return [x[0] + y[0], x[1] + y[1], x[2] + y[2]]

    def sub(x, y):
        return [x[0] - y[0], x[1] - y[1], x[2] - y[2]]

    def det(x, y):
        return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0]]

    def dot(x, y):
        return x[0] * y[0] + x[1] * y[1] + x[2] * y[2]

    P = sub(P2, P1)
    A = sub(A2, A1)

    if norm2(A) == 0:
        return "YES" if R1 + R2 + eps > norm2(P) else "NO"
    elif dot(P, A) > 0:
        return "YES" if R1 + R2 + eps > norm2(P) else "NO"
    else:
        return "YES" if R1 + R2 + eps > abs(norm2(det(P, add(P, A))) / norm2(A)) else "NO"


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        R1, R2 = map(int, input().split())
        P1 = list(map(int, input().split()))
        A1 = list(map(int, input().split()))
        P2 = list(map(int, input().split()))
        A2 = list(map(int, input().split()))

        result = are_spheres_touching(R1, R2, P1, A1, P2, A2)
        print(result)

