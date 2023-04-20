#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Initialize a variable to keep track of the number of deletions
    deletions = 0

    # Iterate through the characters in the string, starting from the second character
    for i in range(1, len(s)):
        # If the current character is the same as the previous character, increment the deletions count
        if s[i] == s[i-1]:
            deletions += 1

    # Return the total number of deletions required to make the string have no matching adjacent characters
    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
