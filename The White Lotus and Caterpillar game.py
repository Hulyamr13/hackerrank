#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def solve(n, m):
    # Write your code here
    r = 0.0

    for l in range(m):
        rr = n - 1.0
        if l >= n:
            rr += (float(l - n + 1)) * (float(l - 1) / float(m))
        if l < m - n:
            rr += (float(m - n - l)) * (float(m - l - 2) / float(m))
        r += rr / float(m)

    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
