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
# The function accepts INTEGER_ARRAY a as parameter.
#
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def solve(a):
    # Write your code here

    sub = False
    a.sort()
    if a[0] == 1:
        sub = True
    result = a[0]
    for i in range(1, len(a)):
        result = gcd(a[i], result)
        if result == 1:
            sub = True
            break
    if sub:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(result + '\n')

    fptr.close()
