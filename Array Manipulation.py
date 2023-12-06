#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n + 1)  # Create an array of zeros, 1-indexed
    for query in queries:
        a, b, k = query[0], query[1], query[2]
        arr[a - 1] += k  # Increment value at index a-1
        arr[b] -= k  # Decrement value at index b
    max_val = 0
    prefix_sum = 0
    for val in arr:
        prefix_sum += val
        max_val = max(max_val, prefix_sum)
    return max_val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
