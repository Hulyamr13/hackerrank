#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxPresentations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY scheduleStart
#  2. INTEGER_ARRAY scheduleEnd
#

def maxPresentations(scheduleStart, scheduleEnd):
    # Write your code here
    presentations = list(zip(scheduleStart, scheduleEnd))

    presentations.sort(key=lambda x: x[1])

    max_presentations = 0
    last_end_time = 0

    for start, end in presentations:
        if start >= last_end_time:
            max_presentations += 1
            last_end_time = end

    return max_presentations


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scheduleStart_count = int(input().strip())

    scheduleStart = []

    for _ in range(scheduleStart_count):
        scheduleStart_item = int(input().strip())
        scheduleStart.append(scheduleStart_item)

    scheduleEnd_count = int(input().strip())

    scheduleEnd = []

    for _ in range(scheduleEnd_count):
        scheduleEnd_item = int(input().strip())
        scheduleEnd.append(scheduleEnd_item)

    result = maxPresentations(scheduleStart, scheduleEnd)

    fptr.write(str(result) + '\n')

    fptr.close()
