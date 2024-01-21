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
#  1. LONG_INTEGER k
#  2. LONG_INTEGER n
#

def solve(k, n):
    # Write your code here
    t = [0]
    for i in range(1, 100):
        t.append((t[-1] + pow(i, n, 100)) % 100)
    return "%02d" % ((t[-1] * (k // 100) + t[k % 100]) % 100)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        k = int(first_multiple_input[0])

        n = int(first_multiple_input[1])

        result = solve(k, n)

        fptr.write(result + '\n')

    fptr.close()
