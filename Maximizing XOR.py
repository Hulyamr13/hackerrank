#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
    # Initialize max_xor to 0
    max_xor = 0

    # Loop through all possible pairs of integers from l to r
    for i in range(l, r+1):
        for j in range(i, r+1):
            # Calculate XOR of current pair
            xor = i ^ j

            # Update max_xor if current XOR is greater
            if xor > max_xor:
                max_xor = xor

    # Return the maximal XOR value
    return max_xor


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()