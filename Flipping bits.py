#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Convert n to its binary representation with 32 bits
    binary = format(n, '032b')

    # Flip all the bits in the binary representation
    flipped_binary = ''.join(['1' if bit == '0' else '0' for bit in binary])

    # Convert the flipped binary representation back to decimal
    result = int(flipped_binary, 2)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
