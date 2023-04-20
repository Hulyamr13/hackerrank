#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    if not s:
        return 0  # If the input string is empty, there are no words

    word_count = 1  # Start with 1 word for the first word in the string
    for char in s:
        if char.isupper():
            word_count += 1  # Increment word count when an uppercase letter is encountered

    return word_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()