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
#  1. INTEGER n
#  2. INTEGER m
#

def solve(a, b):
    m = a
    n = b
    ans = min(((m - 1) * n + (n - 1)), ((n - 1) * m + (m - 1)))
    return m * n - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
