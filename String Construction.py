#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    # Create a set to keep track of unique characters in the string
    unique_chars = set()
    # Iterate through the characters in the string and add them to the set
    for char in s:
        unique_chars.add(char)
    # The minimum cost is equal to the number of unique characters
    return len(unique_chars)

# Test the function with sample inputs
print(stringConstruction("abcd")) # Output: 4
print(stringConstruction("abab")) # Output: 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
