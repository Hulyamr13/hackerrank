#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def solve(n):
    # Write your code here
    tmp = int((2 * n) ** 0.5)
    if tmp * (tmp + 1) == 2 * n:
        return f"Go On Bob {tmp}"
    else:
        return "Better Luck Next Time"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
