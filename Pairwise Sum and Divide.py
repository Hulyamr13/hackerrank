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
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    # Write your code here
    cnt1 = a.count(1)
    cnt2 = a.count(2)
    n = len(a)
    x = [i for i in range(n) if a[i] == 1]

    total_sum = 0
    if cnt2 > 1:
        total_sum += (cnt2 * (cnt2 - 1)) // 2

    if cnt1 > 1:
        total_sum += cnt1 * (cnt1 - 1)

    for i in range(n):
        if a[i] != 1:
            total_sum += cnt1

    return total_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(str(result) + '\n')

    fptr.close()
