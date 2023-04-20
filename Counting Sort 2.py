#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Find the maximum value in the array
    max_val = max(arr)

    # Create a counting array to store the frequency of each value
    counting_arr = [0] * (max_val + 1)

    # Count the frequency of each value in the input array
    for num in arr:
        counting_arr[num] += 1

    # Create a result array to store the sorted values
    result = []

    # Iterate through the counting array and append the values to the result array
    for i in range(len(counting_arr)):
        while counting_arr[i] > 0:
            result.append(i)
            counting_arr[i] -= 1

    return result


# Test the function with the provided sample input
arr = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76,
       85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68,
       78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60,
       65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]
result = countingSort(arr)
print(*result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
