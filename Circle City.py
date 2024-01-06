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
#  1. INTEGER d
#  2. INTEGER k
#

def diviseurs(n):
    div = [1]
    i = 2
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            div.append(i)
            if i != q:
                div.append(q)
        i += 1
    if n != 1:
        div.append(n)
    return div

def solve(d, k):
    d_list = diviseurs(d)
    d1 = sum(1 for i in d_list if i % 4 == 1)
    d3 = sum(1 for i in d_list if i % 4 == 3)
    r2 = 4 * (d1 - d3)
    if k >= r2:
        return "possible"
    else:
        return "impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = solve(d, k)

        fptr.write(result + '\n')

    fptr.close()
