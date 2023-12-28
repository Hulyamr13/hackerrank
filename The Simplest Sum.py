#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simplestSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER a
#  3. INTEGER b
#

MOD = 10 ** 9 + 7


def simplestSum(k, a, b):
    return (s_upto(b, k) - s_upto(a - 1, k)) % MOD


def s_upto(n, k):
    if n == 0:
        return 0

    s, i = 0, 1
    i_seq = []

    while i <= n:
        s += i
        i_seq.append(i)
        i = i * k + 1

    return (s * n - sum(i * (i - 1) for i in i_seq)) % MOD


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        k = int(first_multiple_input[0])

        a = int(first_multiple_input[1])

        b = int(first_multiple_input[2])

        result = simplestSum(k, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

