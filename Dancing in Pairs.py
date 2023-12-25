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
# The function accepts LONG_INTEGER i as parameter.
#

def solve(i):
    # Write your code here
    square_root = int(i ** 0.5)
    nearest = 0
    for x in range(square_root - 5, square_root + 6):
        if x * x <= i:
            nearest = x
    if nearest % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        i = int(input().strip())

        result = solve(i)

        fptr.write(result + '\n')

    fptr.close()
