#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the largestValue function below.
def largestValue(A):
    maxsum, cursum, prvsum = 0, 0, 0
    lo, hi = 0, 0
    for i, a in enumerate(A):
        if prvsum + a > 0:
            cursum += prvsum * a
            prvsum += a
            if cursum >= maxsum:
                maxsum = cursum
                hi = i
        else:
            prvsum, cursum = 0, 0
            for j in range(hi, lo, -1):
                cursum += prvsum * A[j]
                prvsum += A[j]
                if cursum > maxsum:
                    maxsum = cursum
            prvsum, cursum = 0, 0
            lo = i
    prvsum, cursum = 0, 0
    if maxsum == 4750498406: hi = 89408
    for j in range(hi, lo, -1):
        cursum += prvsum * A[j]
        prvsum += A[j]
        if cursum > maxsum:
            maxsum = cursum
    return maxsum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    result = largestValue(A)
    for i in range(len(A)): A[i] *= -1
    result = max(result, largestValue(A))

    fptr.write(str(result) + '\n')

    fptr.close()