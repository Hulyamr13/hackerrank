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
#  1. STRING a
#  2. STRING b
#

MOD = 1000000007


def expn(N, K):
    if K == 0:
        return 1
    if K == 1:
        return N % MOD
    if K % 2 == 0:
        temp = expn(N, K // 2)
        return (temp * temp) % MOD
    else:
        temp = expn(N, K // 2)
        temp = (temp * temp) % MOD
        return (temp * N) % MOD


def solve(a, b):
    arr = [int(x) for x in a]
    brr = [int(x) for x in b]

    temp1 = arr[0] % MOD
    for i in range(1, len(arr)):
        temp1 = (10 * temp1 + arr[i]) % MOD

    temp2 = brr[0] % (MOD - 1)
    for j in range(1, len(brr)):
        temp2 = (10 * temp2 + brr[j]) % (MOD - 1)

    result = expn(temp1, temp2)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = first_multiple_input[0]
        b = first_multiple_input[1]

        result = solve(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

