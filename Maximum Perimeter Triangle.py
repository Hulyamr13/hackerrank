#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True)  # Sort the array in non-increasing order
    n = len(sticks)
    i = 0
    j = 1
    k = 2
    while k < n:
        if sticks[i] < sticks[j] + sticks[k]:
            # Found a non-degenerate triangle
            return [sticks[k], sticks[j], sticks[i]]
        else:
            # Move the pointers to try a smaller value for minimum side
            i += 1
            j += 1
            k += 1
    # No non-degenerate triangle found
    return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()