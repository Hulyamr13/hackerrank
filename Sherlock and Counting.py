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
#  2. INTEGER k
#

def solve(n, k):
    # Write your code here
    if n == 1:
        return 0

    def ok(x):
        return x * (n - x) <= n * k

    if ok(n // 2):
        return n - 1

    if not ok(1):
        return 0

    lo, hi = 1, n // 2

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            lo = mid
        else:
            hi = mid

    return lo * 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = solve(n, k)

        fptr.write(str(result) + '\n')

    fptr.close()
