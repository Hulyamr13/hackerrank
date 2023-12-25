#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER s as parameter.
#

def solve(s):
    # Write your code here
    ll = 1
    rr = s * 4
    while ll < rr:
        mm = (ll + rr) >> 1
        if mm // 2 - mm // 42 < s:
            ll = mm + 1
        else:
            rr = mm
    return ll % (10 ** 9 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = int(input().strip())

        result = solve(s)

        fptr.write(str(result) + '\n')

    fptr.close()
