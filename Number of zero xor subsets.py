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
# The function accepts LONG_INTEGER n as parameter.
#

MOD = 10**9 + 7


def power(a, p, m):
    if p == 2:
        return (a * a) % m
    if p == 0:
        return 1
    if p % 2 == 0:
        return power(power(a, p // 2, m), 2, m)
    return (a * power(a, p - 1, m)) % m


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        result = (power(2, power(2, n, MOD - 1), MOD) * power(power(2, n, MOD), MOD - 2, MOD)) % MOD
        print(result)

