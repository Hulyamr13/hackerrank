#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    # Write your code here
    result = []
    for d in queries:
        minmax = 0
        maxnumber = 0
        for i in range(len(arr)):
            if arr[i] >= maxnumber:
                maxnumber = arr[i]
            elif i >= d:
                if arr[i - d] == maxnumber:
                    maxnumber = max(arr[i - d + 1:i + 1])
            if i >= d - 1:
                if minmax == 0 or minmax > maxnumber:
                    minmax = maxnumber
        result.append(minmax)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
