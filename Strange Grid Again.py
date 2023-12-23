#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'strangeGrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER r
#  2. INTEGER c
#

def strangeGrid(r, c):
    # Write your code here
    if r % 2 != 0:
        return 10 * ((r - 1) // 2) + 2 * (c - 1)

    return 10 * ((r // 2) - 1) + 1 + 2 * (c - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
