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
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#  5. INTEGER xm
#  6. INTEGER ym
#

def solve(x1, y1, x2, y2, xm, ym):
    # Write your code here
    def det(a, b, c, d, e, f):
        return (a - e) * (d - f) - (b - f) * (c - e)

    if det(x1, y1, x2, y2, xm, ym) == 0 and det(x1, y1, x2, y2, 0, 0) == 0:
        return "YES" if (0 - x1) * (xm - x1) >= 0 and (0 - y1) * (ym - y1) >= 0 else "NO"
    elif (
            det(x1, y1, x2, y2, xm, ym) * det(x1, y1, x2, y2, 0, 0) <= 0
            and det(0, 0, xm, ym, x1, y1) * det(0, 0, xm, ym, x2, y2) <= 0
    ):
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        x1 = int(first_multiple_input[0])

        y1 = int(first_multiple_input[1])

        x2 = int(first_multiple_input[2])

        y2 = int(first_multiple_input[3])

        xm = int(first_multiple_input[4])

        ym = int(first_multiple_input[5])

        result = solve(x1, y1, x2, y2, xm, ym)

        fptr.write(result + '\n')

    fptr.close()
