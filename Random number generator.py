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
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        A, B, C = map(int, input().split())
        if C >= A + B:
            print("1/1")
            continue

        denom = 2 * A * B
        if C > B:
            if C > A:
                num = 2 * A * B - (B + A - C) * (A + B - C)
            else:
                num = B * (2 * C - B)
        else:
            if C > A:
                num = A * (2 * C - A)
            else:
                num = C * C

        g = gcd(num, denom)
        print(f"{num // g}/{denom // g}")

