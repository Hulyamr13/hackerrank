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
# The function accepts LONG_INTEGER x as parameter.
#

def solve(x):
    # Write your code here
    low, high = 0, 1000000
    while low <= high:
        mid = (low + high) // 2
        tot = mid * (mid + 1) * (2 * mid + 1) // 6
        next_tot = (mid + 1) * (mid + 2) * (2 * mid + 3) // 6
        prev_tot = mid * (mid - 1) * (2 * mid - 1) // 6
        if tot <= x < next_tot:
            return mid
        elif tot > x >= prev_tot:
            return mid - 1
        elif tot < x:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        x = int(input().strip())

        result = solve(x)

        fptr.write(str(result) + '\n')

    fptr.close()
