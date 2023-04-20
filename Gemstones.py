#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    # Initialize a set to store the minerals in the first rock
    minerals = set(arr[0])

    # Iterate through the remaining rocks
    for rock in arr[1:]:
        # Create a set of minerals in the current rock
        rock_minerals = set(rock)
        # Take the intersection of the current set of minerals and the set of minerals in the first rock
        minerals = minerals.intersection(rock_minerals)

    # Return the count of minerals that are common to all rocks, which represents the number of gemstones
    return len(minerals)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
