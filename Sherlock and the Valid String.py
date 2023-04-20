#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Count the frequency of each character
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    # Count the frequency of each count
    count_freq = {}
    for c in freq.values():
        count_freq[c] = count_freq.get(c, 0) + 1

    # If there is only one count, the string is valid
    if len(count_freq) == 1:
        return "YES"

    # If there are more than two counts, the string is not valid
    if len(count_freq) > 2:
        return "NO"

    counts = list(count_freq.keys())
    # If we can remove only one character
    if (counts[0] == 1 and count_freq[counts[0]] == 1) or (counts[1] == 1 and count_freq[counts[1]] == 1):
        # If one count has frequency 1, the string is valid
        return "YES"
    elif abs(counts[0] - counts[1]) == 1 and (count_freq[counts[0]] == 1 or count_freq[counts[1]] == 1):
        # If the difference between counts is 1 and one count has frequency 1, the string is valid
        return "YES"
    else:
        # Otherwise, the string is not valid
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
