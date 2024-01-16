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
# The function accepts STRING s as parameter.
#

from collections import Counter

MOD = 10**9 + 7

def solve(s):
    num = len(s) // 2
    ca = math.factorial(num)
    cou = Counter(s)

    for i in cou:
        ca = ca // math.factorial(cou[i] // 2)

    return ca % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(str(result) + '\n')
    fptr.close()
