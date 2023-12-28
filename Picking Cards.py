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
# The function accepts INTEGER_ARRAY c as parameter.
#
MOD = 1000000007

def solve(a, n):
    a.sort()
    dp = [0] * (n + 1)
    dp[n] = 1

    for i in range(n - 1, -1, -1):
        low, high = -1, n
        while low + 1 < high:
            mid = low + (high - low) // 2
            if a[mid] <= i:
                low = mid
            else:
                high = mid

        ct = low + 1
        if ct <= i:
            dp[i] = 0
        else:
            dp[i] = (ct - i) * dp[i + 1] % MOD

    return dp[0]


if __name__ == "__main__":
    runs = int(input())
    for _ in range(runs):
        n = int(input())
        a = list(map(int, input().split()))
        for i in range(n):
            if a[i] < 0 or a[i] > n:
                while True:
                    pass
        ret = solve(a, n)
        print(ret)

