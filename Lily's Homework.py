#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    n = len(arr)
    sort = sorted(arr)
    rev = list(reversed(arr))

    d = {}
    for i in range(n):
        if sort[i] not in d:
            d[sort[i]] = i

    swaps = 0
    i = 0
    while i < n:
        if sort[i] == arr[i]:
            i += 1
            continue
        swaps += 1
        arr[d[arr[i]]], arr[i] = arr[i], arr[d[arr[i]]]
        d[sort[i]] += 1

    d = {}
    for i in range(n):
        if sort[i] not in d:
            d[sort[i]] = i

    swaps_rev = 0
    i = 0
    while i < n:
        if sort[i] == rev[i]:
            i += 1
            continue
        swaps_rev += 1
        rev[d[rev[i]]], rev[i] = rev[i], rev[d[rev[i]]]
        d[sort[i]] += 1

    return min(swaps, swaps_rev)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()