#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY points as parameter.
#

def solve(points):
    # Write your code here
    x1, y1, z1 = points[0]
    x2, y2, z2 = points[1]
    x3, y3, z3 = points[2]
    x4, y4, z4 = points[3]

    det = (x1 - x4) * ((y2 - y4) * (z3 - z4) - (y3 - y4) * (z2 - z4)) \
          - (y1 - y4) * ((x2 - x4) * (z3 - z4) - (x3 - x4) * (z2 - z4)) \
          + (z1 - z4) * ((x2 - x4) * (y3 - y4) - (x3 - x4) * (y2 - y4))

    if det == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):

        points = []

        for _ in range(4):
            points.append(list(map(int, input().rstrip().split())))

        result = solve(points)

        fptr.write(result + '\n')

    fptr.close()
