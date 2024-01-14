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
# The function accepts LONG_INTEGER k as parameter.
#

def solve(k):
    # Write your code here
    a = 0
    c = 1
    while k > 0:
        n = int((0.5) * ((8.0 * k + 1.0) ** 0.5 - 1.0))
        if c > 2 and k != 1:
            n = int((0.5) * ((8.0 * k + 9.0) ** 0.5 - 3.0))
            k -= n
        k -= n * (n + 1) // 2
        a += n
        c += 1
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        k = int(input().strip())

        result = solve(k)

        fptr.write(str(result) + '\n')

    fptr.close()
