#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'restaurant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER b
#

def restaurant(l, b):
    # Write your code here
    if l == b:
        return 1

    target = min(l, b)

    while l % target != 0 or b % target != 0:
        target -= 1

    l_cuts = l // target
    b_cuts = b // target

    return l_cuts * b_cuts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()
