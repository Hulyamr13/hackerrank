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
    # extract hours, minutes, and seconds
    hours = int(s[:2])
    minutes = s[3:5]
    seconds = s[6:8]
    meridian = s[8:]

    # convert to military time
    if meridian == 'PM' and hours != 12:
        hours += 12
    elif meridian == 'AM' and hours == 12:
        hours = 0

    # format as string
    military_time = '{:02d}:{:s}:{:s}'.format(hours, minutes, seconds)
    return military_time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
