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
#  3. INTEGER d
#

def solve(a, b, d):
    # Write your code here
    if d == 0:
        return 0
    elif d == a or d == b:
        return 1
    elif d < b:
        return 2
    else:
        if d % b == 0:
            return d // b
        else:
            return d // b + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        d = int(first_multiple_input[2])

        result = solve(a, b, d)

        fptr.write(str(result) + '\n')

    fptr.close()
