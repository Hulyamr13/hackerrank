#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # initialize the variables
    level = 0
    valleys = 0
    # loop through each step in the path
    for step in path:
        # if the step is uphill, increment the level
        if step == 'U':
            level += 1
        # if the step is downhill, decrement the level
        elif step == 'D':
            level -= 1
            # if the level is -1, the hiker has entered a valley
            if level == -1:
                valleys += 1
    return valleys



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()