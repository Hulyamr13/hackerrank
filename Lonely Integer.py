#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Initialize a dictionary to store counts of each element
    counts = {}

    # Loop through the array and update counts
    for num in a:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Find the unique element with count == 1
    for num, count in counts.items():
        if count == 1:
            return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()