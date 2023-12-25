#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'closestNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER x
#

def closestNumber(a, b, x):
    # Write your code here
    result = int(math.pow(a, b))

    closest_multiple = round(result / x) * x

    return closest_multiple


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        x = int(first_multiple_input[2])

        result = closestNumber(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()
