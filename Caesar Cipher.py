#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    encrypted = ""
    for char in s:
        if char.isalpha():
            # Determine the base of the alphabet (lowercase or uppercase)
            base = ord('a') if char.islower() else ord('A')
            # Calculate the shifted position
            shifted_pos = (ord(char) - base + k) % 26
            # Convert back to ASCII code and add the base
            encrypted_char = chr(shifted_pos + base)
            encrypted += encrypted_char
        else:
            # For non-alphabetic characters, keep them unchanged
            encrypted += char

    return encrypted


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()