#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Calculate the number of pages to turn from the front of the book
    front_turns = p // 2

    # Calculate the number of pages to turn from the back of the book
    back_turns = (n // 2) - (p // 2)

    # Return the minimum of front_turns and back_turns
    return min(front_turns, back_turns)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()