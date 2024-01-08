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
# The function accepts following parameters:
#  1. LONG_INTEGER l
#  2. LONG_INTEGER r
#

def len_digit(num):
    digits = 0
    while num != 0:
        num //= 10
        digits += 1
    return digits

def solve(l, r):
    upper_bound = 1000000000000000000
    s = set()
    q = [0] * 500
    head = tail = 0

    for i in range(10):
        q[tail] = i
        tail += 1
        s.add(i)

    while head < tail:
        num = q[head]
        head += 1
        num_len = len_digit(num)
        for i in range(num_len, num_len + 3):
            candidate = num * i
            if candidate not in s and len_digit(candidate) == i and candidate <= upper_bound:
                q[tail] = candidate
                tail += 1
                s.add(candidate)

    count = sum(1 for i in q[:tail] if l <= i <= r)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = solve(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
