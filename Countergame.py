#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#


def get_turn(turns):
    return "Richard" if turns % 2 == 0 else "Louise"


def npot(x):
    exp = math.floor(math.log(x, 2))
    r = int(math.pow(2, exp))
    return r


def counterGame(n):
    turns = 0
    while n > 1:
        np = npot(n)
        if np == n:
            n >>= 1
        else:
            n -= np
        turns += 1
    return get_turn(turns)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
