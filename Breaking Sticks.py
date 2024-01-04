#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestSequence' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY a as parameter.
#

def factorize(x):
    factors = []
    while x % 2 == 0:
        factors.append(2)
        x //= 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            factors.append(i)
            x //= i
    if x > 2:
        factors.append(x)
    return factors

def solve(x):
    factors = factorize(x)
    prod = 1
    ans = x
    for j in sorted(factors, reverse=True):
        ans += prod
        prod *= j
    return ans

def longestSequence(a):
    ans = 0
    for i in a:
        ans += solve(i)
    return ans

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    result = longestSequence(a)
    print(result)