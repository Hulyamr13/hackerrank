#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    # Write your code here
    n = len(a)
    b = [a[0]]

    for i in range(n - 1):
        b.append(a[i] * a[i + 1] // math.gcd(a[i], a[i + 1]))

    b.append(a[n - 1])
    return b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
