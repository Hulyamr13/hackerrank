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
#  1. INTEGER d
#  2. INTEGER p
#

def solve(d, p):
    if d == 0:
        if p < 0:
            return 0
        else:
            n = int(math.sqrt(p))
            if n * n == p:
                if n == 0:
                    return 1
                else:
                    return 2
            else:
                return 0
    elif d < 0:
        return 0
    else:
        x = d * d + 4 * p
        if x < 0:
            return 0
        elif x == 0:
            return 2
        else:
            y = int(math.sqrt(x))
            if (y + 1) * (y + 1) == x:
                y += 1
            if (y - 1) * (y - 1) == x:
                y -= 1
            if y * y == x:
                return 4
            else:
                return 0


if __name__ == "__main__":
    ntest = int(input().strip())
    for _ in range(ntest):
        d, p = map(int, input().split())
        result = solve(d, p)
        print(result)

