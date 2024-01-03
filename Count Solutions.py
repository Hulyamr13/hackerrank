#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countSolutions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#  4. INTEGER d
#

def countSolutions(a, b, c, d):
    # Write your code here
    ans = {}
    t = 0
    for i in range(1, c + 1):
        gg = i * (i - a)
        if gg in ans:
            ans[gg] += 1
        else:
            ans[gg] = 1
    for i in range(1, d + 1):
        gg = i * (b - i)
        if gg in ans:
            t += ans[gg]
    return t


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        d = int(first_multiple_input[3])

        result = countSolutions(a, b, c, d)

        fptr.write(str(result) + '\n')

    fptr.close()
