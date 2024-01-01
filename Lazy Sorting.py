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
# The function accepts INTEGER_ARRAY P as parameter.
#

def solve(P):
    # Write your code here
    q = P[:]
    q.sort()
    if P == q:
        return 0
    l = {}
    f = math.factorial(len(P))
    for i in range(len(P)):
        if P[i] in l:
            l[P[i]] += 1
        else:
            l[P[i]] = 1
    P = list(set(P))
    for i in range(len(P)):
        f = f / (math.factorial(l[P[i]]))
    return round(f, 6)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    P_count = int(input().strip())

    P = list(map(int, input().rstrip().split()))

    result = solve(P)

    fptr.write(str(result) + '\n')

    fptr.close()
