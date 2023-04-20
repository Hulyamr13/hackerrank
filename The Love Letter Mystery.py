#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    # Initialize a variable to keep track of the total number of operations
    operations = 0

    # Convert the string to a list of characters to make it mutable
    s = list(s)

    # Loop through the first half of the string
    for i in range(len(s) // 2):
        # Calculate the ASCII difference between the characters at the beginning and end of the string
        diff = ord(s[i]) - ord(s[-i-1])
        # Add the absolute value of the difference to the total number of operations
        operations += abs(diff)

    # Return the total number of operations
    return operations


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
