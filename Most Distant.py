#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    # Write your code here
    max_x = float('-inf')
    min_x = float('inf')
    max_y = float('-inf')
    min_y = float('inf')

    for x, y in coordinates:
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)

    max_distance = max(max_x - min_x, max_y - min_y)
    max_distance = max(max_distance, math.sqrt(max_x * max_x + max_y * max_y))
    max_distance = max(max_distance, math.sqrt(max_x * max_x + min_y * min_y))
    max_distance = max(max_distance, math.sqrt(min_x * min_x + max_y * max_y))
    max_distance = max(max_distance, math.sqrt(min_x * min_x + min_y * min_y))

    return round(max_distance, 6)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
