#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoSubsequences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER r
#  3. INTEGER s
#
mod = 10 ** 9 + 7


def twoSubsequences(x, r, s):
    # Write your code here
    if r < s or (r + s) % 2 == 1 or r == 0:
        return 0
    h, l = (r + s) // 2, (r - s) // 2
    m = len(x)
    dp = [[0 for i in range(m + 1)] for j in range(h + 1)]
    dp[0][0] = 1
    if x[0] <= h:
        dp[x[0]][1] = 1
    for i in range(1, m):
        for j in range(h, 0, -1):
            for k in range(1, m + 1):
                if j >= x[i]:
                    dp[j][k] = (dp[j][k] + dp[j - x[i]][k - 1]) % mod
    res = 0
    for k in range(1, m + 1):
        res = (res + dp[h][k] * dp[l][k]) % mod
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    r = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    x = list(map(int, input().rstrip().split()))

    result = twoSubsequences(x, r, s)

    fptr.write(str(result) + '\n')

    fptr.close()