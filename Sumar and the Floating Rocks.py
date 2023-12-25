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
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#

def solve(x1, y1, x2, y2):
    # Write your code here
    if x1 == x2:
        return abs(y2 - y1) - 1
    elif y1 == y2:
        return abs(x2 - x1) - 1
    else:
        return math.gcd(abs(x2 - x1), abs(y2 - y1)) - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        x1 = int(first_multiple_input[0])

        y1 = int(first_multiple_input[1])

        x2 = int(first_multiple_input[2])

        y2 = int(first_multiple_input[3])

        result = solve(x1, y1, x2, y2)

        fptr.write(str(result) + '\n')

    fptr.close()
