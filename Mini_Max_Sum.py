#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()  # Sort the array in ascending order
    min_sum = sum(arr[:4])  # Calculate the minimum sum by summing the first four elements
    max_sum = sum(arr[1:])  # Calculate the maximum sum by summing the last four elements
    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
