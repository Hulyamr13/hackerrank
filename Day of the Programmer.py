#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    if year == 1918:
        # special case for year 1918
        return '26.09.1918'
    elif year < 1918:
        # Julian calendar system
        leap = year % 4 == 0
    else:
        # Gregorian calendar system
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    if leap:
        days_in_feb = 29
    else:
        days_in_feb = 28
    days_in_month = [31, days_in_feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_up_to_sept = sum(days_in_month[:8])
    day_of_programmer = 256 - days_up_to_sept
    return f"{day_of_programmer:02d}.09.{year}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()