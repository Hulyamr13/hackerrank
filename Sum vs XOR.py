#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Initialize count to 0
    count = 0

    # Count the number of zeros in the binary representation of n
    while n > 0:
        # If the current bit is 0, increment count
        if n % 2 == 0:
            count += 1
        # Right shift n by 1 bit
        n >>= 1

    # Return 2 raised to the power of count as the result
    return 2 ** count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()