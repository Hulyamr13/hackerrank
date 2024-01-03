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
#  1. INTEGER a
#  2. INTEGER b
#  3. LONG_INTEGER t
#

def solve(a, b, t):
    # Write your code here
    result = pow((a + b) // 2, t, 10 ** 9 + 7)
    return int(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])

    b = int(first_multiple_input[1])

    t = int(first_multiple_input[2])

    result = solve(a, b, t)

    fptr.write(str(result) + '\n')

    fptr.close()
