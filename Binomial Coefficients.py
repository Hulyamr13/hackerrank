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
#  1. STRING n
#  2. INTEGER p
#

def calculate(n, p):
    if n == 0 or n == 1:
        return 0

    cb = n
    ans = 1
    while cb != 0:
        ans *= cb % p + 1
        cb //= p

    return n + 1 - ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, p = map(int, input().split())
        result = calculate(n, p)
        print(result)

