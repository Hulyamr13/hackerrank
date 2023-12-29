#!/bin/python3

from math import atan2, pi
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    # Write your code here
    sorted_coords = sorted(
        coordinates,
        key=lambda x: (atan2(x[1], x[0]) % (2 * pi), x[0] ** 2 + x[1] ** 2)
    )
    return sorted_coords


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
