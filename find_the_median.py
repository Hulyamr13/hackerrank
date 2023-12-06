#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr.sort()

    # Calculate the length of the array
    length = len(arr)

    # Check if the length of the array is odd or even
    if length % 2 == 0:
        # If the length is even, take the average of the two middle elements
        median = (arr[length // 2 - 1] + arr[length // 2]) / 2
    else:
        # If the length is odd, take the middle element
        median = arr[length // 2]

    return int(median)  # Return the median as an integer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
