#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Create dictionaries to store character counts for each string
    dict1 = {}
    dict2 = {}

    # Iterate through s1 and populate dict1 with character counts
    for char in s1:
        dict1[char] = dict1.get(char, 0) + 1

    # Iterate through s2 and populate dict2 with character counts
    for char in s2:
        dict2[char] = dict2.get(char, 0) + 1

    # Initialize the number of deletions needed to 0
    deletions = 0

    # Iterate through the characters in dict1
    for char in dict1:
        # If the character is not found in dict2, add its count to deletions
        if char not in dict2:
            deletions += dict1[char]
        # If the character is found in dict2, subtract the minimum count from both dicts
        else:
            deletions += max(dict1[char] - dict2[char], 0)
            dict2[char] = max(dict2[char] - dict1[char], 0)

    # Iterate through the characters in dict2 to account for characters not present in dict1
    for char in dict2:
        deletions += dict2[char]

    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()