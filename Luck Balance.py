#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    important = []
    unimportant = []
    total_luck = 0

    # Separate contests into important and unimportant
    for contest in contests:
        if contest[1] == 1:
            important.append(contest[0])
        else:
            unimportant.append(contest[0])

    # Sort important contests in descending order of luck balance
    important.sort(reverse=True)

    # Calculate total luck balance for unimportant contests
    total_luck = sum(unimportant)

    # Add luck balance of first k important contests to total luck balance
    # Subtract luck balance of remaining important contests from total luck balance
    for i in range(len(important)):
        if i < k:
            total_luck += important[i]
        else:
            total_luck -= important[i]

    return total_luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()