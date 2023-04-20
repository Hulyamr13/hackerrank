#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Create a set of characters from s1
    set_s1 = set(s1)
    # Iterate through characters in s2 and check if any character is in set_s1
    for char in s2:
        if char in set_s1:
            return "YES"  # If a common character is found, return "YES"
    return "NO"  # If no common character is found, return "NO"

# Test the function with sample inputs
print(twoStrings("hello", "world")) # Output: "YES"
print(twoStrings("hi", "world")) # Output: "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
