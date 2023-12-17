#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#
from heapq import *


def runningMedian(a):
    # Write your code here
    under = []
    upper = []
    medians = []

    for curNumber in a:
        if len(upper) == 0:
            upper.append(curNumber)
            medians.append(curNumber)
            continue

        middle = upper[0]
        if curNumber >= middle:
            heappush(upper, curNumber)
        else:
            heappush(under, -curNumber)

        if len(under) >= len(upper):
            heappush(upper, -heappop(under))

        if len(upper) >= len(under) + 2:
            heappush(under, -heappop(upper))

        if (len(upper) + len(under)) % 2 == 1:
            medians.append(float(upper[0]))
        else:
            medians.append((float(upper[0]) + -under[0]) / 2)

    return medians


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
