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
# The function accepts INTEGER n as parameter.
#

def solve(n):
    # Write your code here
    divisors = [[1] for i in range(n)]
    for i in range(2, n):
        for j in range(i, n, i):
            divisors[j].append(i)
        divisors[i].reverse()

    tups = 0
    for i in range(1, n):
        divs = set()
        for j in range(i, n, i):
            divisors[j].pop()
        for j in range(i, n, i):
            divs.update(divisors[n - j])
        tups += len(divs)

    return tups


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()
