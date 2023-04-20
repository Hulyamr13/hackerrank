#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nimGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY pile as parameter.
#

def nimGame(pile):
    # XOR of all pile sizes
    xor_sum = 0
    for stones in pile:
        xor_sum ^= stones

    # If XOR sum is 0, it means player 2 will win, otherwise player 1 will win
    if xor_sum == 0:
        return "Second"
    else:
        return "First"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        fptr.write(result + '\n')

    fptr.close()
