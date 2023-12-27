#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerColoring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def power(x, y, p):
    res = 1
    x = x % p

    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p

    return res


def towerColoring(n):
    p = 10**9 + 7
    yy = power(3, n, p - 1) % (p - 1)
    res = power(3, yy, p) % p
    return res


if __name__ == '__main__':
    n = int(input().strip())
    result = towerColoring(n)
    print(result)
