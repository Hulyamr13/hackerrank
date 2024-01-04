#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER l
#  2. LONG_INTEGER r
#
from bisect import bisect_right


def calculate_euler():
    euler = [0] * 2000001
    for i in range(1, 2000001):
        euler[i] += i
        for j in range(2 * i, 2000001, i):
            euler[j] -= euler[i]
    return euler


def calculate_values_and_sums(euler):
    V, ans = [], []
    for i in range(0, 2000000, 2):
        V.extend([(i * (i + 1)) // 2, ((i + 2) * (i + 1)) // 2])
        ans.extend([euler[i // 2] * euler[i + 1], euler[(i // 2) + 1] * euler[i + 1]])

    for i in range(1, 2000000):
        ans[i] += ans[i - 1]

    return V, ans


def main():
    euler = calculate_euler()
    V, ans = calculate_values_and_sums(euler)

    T = int(input())
    for _ in range(T):
        L, R = map(int, input().split())
        L -= 1
        result = ans[bisect_right(V, R) - 1] - ans[bisect_right(V, L) - 1]
        print(result)


if __name__ == "__main__":
    main()
