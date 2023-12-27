#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pythagoreanTriple' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER a as parameter.
#

def pythagoreanTriple(a):
    # Write your code here
    if a < 3:
        return [-1]

    if a % 2 == 0:
        m = a // 2
        n = 1
        triple = [a, m ** 2 - n ** 2, m ** 2 + n ** 2]
    else:
        m = (a + 1) // 2
        n = (a - 1) // 2
        triple = [a, 2 * m * n, m ** 2 + n ** 2]

    return triple


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input().strip())

    triple = pythagoreanTriple(a)

    fptr.write(' '.join(map(str, triple)))
    fptr.write('\n')

    fptr.close()
