#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    # Write your code here
    stack = []
    max_days = 0

    for i, pesticide in enumerate(p):
        days = 0

        # While the stack isn't empty and the current pesticide is greater than the left plant
        while stack and pesticide <= stack[-1][0]:
            _, d = stack.pop()
            days = max(days, d)

        # If stack isn't empty, it means the current plant is stronger than the left
        if stack:
            days += 1

        max_days = max(max_days, days)
        stack.append((pesticide, days))

    return max_days



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
