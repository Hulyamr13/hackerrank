#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappush, heappop

def solve(A, B, C):
    M = 1000000007
    mps = {}

    for x, y in zip(B, C):
        if x not in mps:
            mps[x] = y
        else:
            mps[x] = (mps[x] * y) % M

    q = []

    for k in mps:
        heappush(q, (k, k, mps[k]))

    while len(q) > 0:
        ix, k, y = heappop(q)
        if ix > len(A):
            break
        A[ix - 1] = (A[ix - 1] * y) % M
        heappush(q, (ix + k, k, y))

    return A

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    C = list(map(int, input().rstrip().split()))

    result = solve(A, B, C)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
