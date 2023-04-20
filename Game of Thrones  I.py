#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Create a dictionary to store character frequencies
    char_freq = {}
    # Iterate through the string and count the frequency of each character
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Count the number of characters with odd frequency
    odd_freq_count = 0
    for freq in char_freq.values():
        if freq % 2 != 0:
            odd_freq_count += 1

    # If the number of characters with odd frequency is at most 1, the string can be rearranged into a palindrome
    if odd_freq_count <= 1:
        return "YES"
    else:
        return "NO"

# Test the function with sample inputs
print(gameOfThrones("aaabbbb")) # Output: "YES"
print(gameOfThrones("cdefghmnopqrstuvw")) # Output: "NO"
print(gameOfThrones("cdcdcdcdeeeef")) # Output: "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
