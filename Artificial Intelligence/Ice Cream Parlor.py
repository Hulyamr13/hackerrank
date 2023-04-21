#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Create a dictionary to store the costs and their corresponding indices
    cost_dict = {}

    # Loop through the array of costs
    for i, cost in enumerate(arr):
        # Calculate the remaining amount of money after buying the current flavor
        remaining = m - cost
        # If the remaining amount is in the dictionary, it means we found a pair of flavors that meet the criteria
        if remaining in cost_dict:
            # Return the indices of the two flavors sorted ascendingly
            return [cost_dict[remaining] + 1, i + 1]
        # If the remaining amount is not in the dictionary, add the current cost and its index to the dictionary
        cost_dict[cost] = i

# Example usage:
m = 4
arr = [1, 4, 5, 3, 2]
result = icecreamParlor(m, arr)
print(result)  # Output: [1, 4]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()