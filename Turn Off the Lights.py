#!/bin/python3

import os
import sys


def get_sum(s, c, k, t):
    v = None
    for p in range(s, len(c), 2 * k + 1):
        print(p, end=' ')
        if v:
            t += 2 * k + 1
        else:
            v = 0

        v += c[p]

    if t < len(c):
        v = None

    print(' => ', v, 't=', t)
    return v


#
# Complete the turnOffTheLights function below.
#
def turnOffTheLights(k, c):
    min_sum = None
    for s in range(k + 1):
        summ = get_sum(s, c, k, k + 1 + s)
        if not min_sum or (summ and min_sum > summ):
            min_sum = summ

    return min_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, k = map(int, input().split())
    c = list(map(int, input().rstrip().split()))

    result = turnOffTheLights(k, c)
    fptr.write(str(result) + '\n')
    fptr.close()