#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Convert the input string to lowercase and remove whitespace
    s = s.lower().replace(" ", "")

    # Create a set to store unique characters
    unique_chars = set()

    # Iterate through each character in the string
    for char in s:
        # Add the character to the set if it's an alphabet
        if char.isalpha():
            unique_chars.add(char)

    # If the set contains all 26 alphabets, it's a pangram
    if len(unique_chars) == 26:
        return "pangram"
    else:
        return "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()