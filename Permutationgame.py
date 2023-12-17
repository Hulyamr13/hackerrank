#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'permutationGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def permutationGame(arr):
    # Write your code here
    def canWin(arr):
        if sorted(arr) == arr:
            return False

        if tuple(arr) in memo:
            return memo[tuple(arr)]

        for i in range(len(arr)):
            temp = arr[:i] + arr[i + 1:]
            if not canWin(temp):
                memo[tuple(arr)] = True
                return True

        memo[tuple(arr)] = False
        return False

    memo = {}
    return "Alice" if canWin(arr) else "Bob"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = permutationGame(arr)

        fptr.write(result + '\n')

    fptr.close()
