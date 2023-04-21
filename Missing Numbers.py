#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Initialize dictionaries to store frequency of numbers in arr and brr
    freq_arr = {}
    freq_brr = {}

    # Iterate through arr and update freq_arr dictionary
    for num in arr:
        if num in freq_arr:
            freq_arr[num] += 1
        else:
            freq_arr[num] = 1

    # Iterate through brr and update freq_brr dictionary
    for num in brr:
        if num in freq_brr:
            freq_brr[num] += 1
        else:
            freq_brr[num] = 1

    # Initialize a list to store missing numbers
    missing_nums = []

    # Compare freq_arr and freq_brr to find missing numbers
    for num in freq_brr:
        # If num is not present in freq_arr or its frequency is different, it's a missing number
        if num not in freq_arr or freq_brr[num] > freq_arr[num]:
            missing_nums.append(num)

    # Sort the missing numbers in ascending order
    missing_nums.sort()

    return missing_nums


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()