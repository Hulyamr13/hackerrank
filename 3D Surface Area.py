#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    H, W = len(A), len(A[0])
    area = 2 * H * W  # top and bottom surfaces

    # add front and back surfaces
    for i in range(H):
        for j in range(W):
            if j == 0:
                area += A[i][j]
            else:
                area += abs(A[i][j] - A[i][j-1])
            if j == W-1:
                area += A[i][j]

    # add left and right surfaces
    for j in range(W):
        for i in range(H):
            if i == 0:
                area += A[i][j]
            else:
                area += abs(A[i][j] - A[i-1][j])
            if i == H-1:
                area += A[i][j]

    return area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()