#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY stars as parameter.
#

def solve(stars):
    # Write your code here
    n = len(stars)
    best = 0

    for i in range(n):
        for j in range(i + 1, n):
            sum1, sum2 = 0, 0
            for k in range(n):
                sign = ((stars[k][1] - stars[i][1]) * (stars[j][0] - stars[i][0]) -
                        (stars[k][0] - stars[i][0]) * (stars[j][1] - stars[i][1]))
                if sign < 0:
                    sum1 += stars[k][2]
                elif sign > 0:
                    sum2 += stars[k][2]

            best = max(best, max(
                max(min(sum1 + stars[i][2], sum2 + stars[j][2]), min(sum1 + stars[j][2], sum2 + stars[i][2])),
                max(min(sum1 + stars[i][2] + stars[j][2], sum2), min(sum1, sum2 + stars[i][2] + stars[j][2])))
                       )

    return best


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    stars = []

    for _ in range(n):
        stars.append(list(map(int, input().rstrip().split())))

    result = solve(stars)

    fptr.write(str(result) + '\n')

    fptr.close()
