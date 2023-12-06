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
    # Write your code here
    encrypted = ""
    for char in s:
        if char.isalpha():

            base = ord('a') if char.islower() else ord('A')

            shifted_pos = (ord(char) - base + k) % 26

            encrypted_char = chr(shifted_pos + base)
            encrypted += encrypted_char
        else:

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
