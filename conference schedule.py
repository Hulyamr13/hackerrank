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
    schedules = [(start, end) for start, end in zip(scheduleStart, scheduleEnd)]

    schedules.sort(key=lambda x: x[1])

    max_end_time = -1
    presentation_count = 0

    for start, end in schedules:
        if start >= max_end_time:
            max_end_time = end
            presentation_count += 1

    return presentation_count


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
