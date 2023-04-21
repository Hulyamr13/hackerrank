#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    # Sort the calorie counts in descending order
    calorie.sort(reverse=True)

    # Initialize the minimum miles to walk to 0
    min_miles = 0

    # Calculate the minimum miles by summing up the product of calorie count and 2 raised to the power of index
    for i in range(len(calorie)):
        min_miles += calorie[i] * (2 ** i)

    # Return the minimum miles
    return min_miles


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()