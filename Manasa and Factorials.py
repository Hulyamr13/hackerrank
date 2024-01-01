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
# The function accepts LONG_INTEGER n as parameter.
#

def countingTrailingZeros(m):
    if m == 0:
        return 0
    return m // 5 + countingTrailingZeros(m // 5)


def solve(n):
    res = -1
    l = 0
    u = 5 * n

    while l <= u:
        mid = (l + u) // 2

        if countingTrailingZeros(mid) >= n:
            res = mid
            u = mid - 1
        else:
            l = mid + 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()
