#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Calculate the total sum of the array
    total_sum = sum(arr)

    # Initialize the left sum to 0
    left_sum = 0

    # Iterate through the array to find an element with equal left and right sum
    for num in arr:
        # Update the total sum by subtracting the current element
        total_sum -= num

        # If the left sum is equal to the total sum (right sum), return "YES"
        if left_sum == total_sum:
            return "YES"

        # Update the left sum by adding the current element
        left_sum += num

    # If no such element is found, return "NO"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()