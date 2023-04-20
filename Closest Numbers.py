#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()  # Sort the input array

    min_diff = float('inf')  # Initialize min_diff to a large positive number
    result = []  # Initialize result list

    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i-1])  # Calculate absolute difference between pairs

        if diff < min_diff:
            min_diff = diff
            result = [(arr[i-1], arr[i])]  # Update result list with current pair
        elif diff == min_diff:
            result.append((arr[i-1], arr[i]))  # Append current pair to result list

    # Flatten the result list and return as integers
    return [num for pair in result for num in pair]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
