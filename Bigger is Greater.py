#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Find the index i of the last character in w such that w[i-1] < w[i]
    i = len(w) - 1
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1

    # If no such character exists, w is already the largest permutation
    if i == 0:
        return "no answer"

    # Find the index j of the smallest character to the right of i-1 and greater than w[i-1]
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1

    # Swap the characters at indices i-1 and j
    w = list(w)
    w[i - 1], w[j] = w[j], w[i - 1]

    # Reverse the substring w[i:]
    w[i:] = reversed(w[i:])

    return ''.join(w)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()