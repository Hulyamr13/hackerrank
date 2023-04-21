#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Sort the array in ascending order
    arr.sort()

    # Initialize the minimum absolute difference to a large value
    min_abs_diff = float('inf')

    # Iterate through the sorted array and calculate the absolute difference between adjacent elements
    for i in range(len(arr) - 1):
        abs_diff = abs(arr[i] - arr[i + 1])

        # Update the minimum absolute difference if the current absolute difference is smaller
        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff

    # Return the minimum absolute difference
    return min_abs_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
