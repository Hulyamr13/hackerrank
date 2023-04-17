#!/bin/python3

import math
import os
import random
import re
import sys

def timeInWords(h, m):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
             "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
             "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven",
             "twenty eight", "twenty nine"]

    if m == 0:
        return f"{words[h-1]} o' clock"
    elif m == 1:
        return f"{words[m-1]} minute past {words[h-1]}"
    elif m == 15:
        return f"quarter past {words[h-1]}"
    elif m < 30:
        return f"{words[m-1]} minutes past {words[h-1]}"
    elif m == 30:
        return f"half past {words[h-1]}"
    elif m == 45:
        return f"quarter to {words[h%12]}"
    else:
        return f"{words[60-m-1]} minutes to {words[h%12]}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()