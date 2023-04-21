#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    prices.sort()  # Sort the prices in ascending order
    count = 0  # Initialize count to keep track of number of toys
    total_cost = 0  # Initialize total_cost to keep track of total cost

    # Iterate through the sorted prices list and increment count and total_cost
    # until total_cost exceeds k
    for price in prices:
        if total_cost + price <= k:
            count += 1
            total_cost += price
        else:
            break

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()