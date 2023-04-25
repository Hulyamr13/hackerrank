#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countArray function below.
def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    if x != 1:
        endx = 0
        end = 1
    else:
        endx = 1
        end = 0
    for i in range(2, n + 1):
        endx, end = end, (end * (k - 2) + endx * (k - 1)) % (1000000000 + 7)
    return endx % (1000000000 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()