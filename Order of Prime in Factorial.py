#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER p
#  2. LONG_INTEGER l
#

def solve(p, l):
    # Write your code here
    a = (l // p) // p
    b = (l // p) % p
    c = l % p
    ans = 0

    if a > 0:
        ans += a * p

    aux = 0

    while a:
        aux += a
        a //= p

    aux %= p

    if aux > 0:
        aux = p - aux

    if aux < b:
        ans += p
    elif aux == b:
        ans += c + 1

    return ans - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = int(first_multiple_input[0])

        l = int(first_multiple_input[1])

        result = solve(p, l)

        fptr.write(str(result) + '\n')

    fptr.close()
