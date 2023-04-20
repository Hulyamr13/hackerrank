#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    # Initialize a variable to keep track of the number of steps
    steps = 0

    # Convert the binary string to a list to make it mutable
    b = list(b)

    # Iterate through the binary string, starting from the third character
    for i in range(2, len(b)):
        # Check if the current character and the previous two characters form the substring "010"
        if b[i] == '0' and b[i-1] == '1' and b[i-2] == '0':
            # Change the current character from '0' to '1' or vice versa to make the string beautiful
            steps += 1
            # Update the next character to '1' if the current character is '0', or '0' if the current character is '1'
            b[i] = '1' if b[i] == '0' else '0'

    # Return the total number of steps needed to make the string beautiful
    return steps



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
