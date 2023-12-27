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
#  1. INTEGER n
#  2. INTEGER m
#
MOD = 10**9 + 7

def calculate_factorials(N, M):
    factorials = [1] * (min(N, M) + 1)
    for i in range(1, min(N, M) + 1):
        factorials[i] = factorials[i - 1] * i % MOD
    return factorials


def calculate_result(N, M, factorials):
    result = 1
    for i in range(1, N):
        result = result * factorials[min(i, M)] % MOD
    for i in range(M):
        result = result * factorials[min(N, M - i)] % MOD
    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    factorials = calculate_factorials(N, M)
    result = calculate_result(N, M, factorials)
    print(result)
