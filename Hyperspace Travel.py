#!/bin/python3

import math
import os
import random
import re
import sys
import operator


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY friends as parameter.
#

def solve(friends):
    # Write your code here
    lines = len(friends)
    dim = len(friends[0])
    points = friends
    coords = map(sorted, zip(*points))
    getter = operator.itemgetter((lines - 1) // 2)
    return list(map(getter, coords))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    friends = []

    for _ in range(n):
        friends.append(list(map(int, input().rstrip().split())))

    result = solve(friends)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
