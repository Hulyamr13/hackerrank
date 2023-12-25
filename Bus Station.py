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
    s = set()

    cur = a[0]
    s.add(cur)

    for i in range(1, len(a)):
        cur += a[i]
        s.add(cur)

    res = []

    for item in sorted(s):
        if cur % item == 0:
            flag = True
            for j in range(1, cur // item + 1):
                if item * j not in s:
                    flag = False
                    break
            if flag:
                res.append(item)

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
