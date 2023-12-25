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
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    # Write your code here
    mod = pow(10, 9) + 7
    c = 0
    for i in a:
        if i % 2 == 1:
            c = 1
            break

    r = 1
    for i in range(1, len(a) - c + 1):
        r = (r * 2) % mod

    return (r - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()
