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
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING s
#

from fractions import Fraction

def solve(n, k, s):
    r = 0
    cs = 0
    for i in range(len(s)):
        if s[i] == '1':
            r += cs
        cs += (s[i] == '1')
        if i >= k:
            cs -= (s[i - k] == '1')
    r *= 2
    r += s.count('1')
    res = Fraction(r, n * n)
    return f"{res.numerator}/{res.denominator}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        s = input().strip()

        result = solve(n, k, s)

        fptr.write(result + '\n')

    fptr.close()

