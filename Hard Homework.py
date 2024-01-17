#!/bin/python3

import os

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts INTEGER n as parameter.
#

from math import sin, cos


def solve(n):
    maxc = [False, False, 1, max(cos(-1 / 2), cos(1 / 2)), 1]
    for i in range(5, n):
        maxc.append(max(cos(i / 2 - 1), cos(1 - i / 2), maxc[-2]))

    res = -3
    for i in range(1, n - 1):
        res = max(res, sin(i) + 2 * sin((n - i) / 2) * maxc[n - i])

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = solve(n)

    fptr.write('{:.9f}'.format(result) + '\n')

    fptr.close()
