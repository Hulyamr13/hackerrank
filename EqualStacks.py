#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    h1.reverse()
    h2.reverse()
    h3.reverse()

    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)

    while not (sum_h1 == sum_h2 == sum_h3):
        maximum = max(sum_h1, sum_h2, sum_h3)
        if maximum == sum_h1:
            sum_h1 -= h1.pop()
        elif maximum == sum_h2:
            sum_h2 -= h2.pop()
        elif maximum == sum_h3:
            sum_h3 -= h3.pop()

    return sum_h1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
