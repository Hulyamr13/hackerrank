#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time_parts = s.split(':')
    seconds = time_parts[2][:2]
    period = time_parts[2][-2:]

    if period == 'AM':
        if time_parts[0] == '12':
            time_parts[0] = '00'
    else:
        if time_parts[0] != '12':
            time_parts[0] = str(int(time_parts[0]) + 12)

    military_time = ':'.join([str(elem) for elem in time_parts[:2]]) + ':' + seconds

    return military_time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
