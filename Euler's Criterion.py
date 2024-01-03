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
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER m
#

def mod_binary(a, e, m):
    if e == 1:
        return a % m
    elif e == 0:
        return 1
    else:
        result = mod_binary(a, e // 2, m)
        if e % 2 == 1:
            temp = (result * result) % m
            temp = (temp * a) % m
            return temp
        else:
            return (result * result) % m


def solve(a, m):
    result = mod_binary(a, (m - 1) // 2, m)
    if result == 1 or a == 0 or a == 2:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(a, m)

        fptr.write(result + '\n')

    fptr.close()
