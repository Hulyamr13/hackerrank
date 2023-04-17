#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Initialize a variable to keep track of the total number of loaves distributed
    total_loaves = 0

    # Loop through the array of loaves
    for i in range(len(B)):
        # If the current person has an odd number of loaves
        if B[i] % 2 != 0:
            # Check if there is a next person in line to give a loaf to
            if i < len(B) - 1:
                B[i] += 1
                B[i + 1] += 1
                total_loaves += 2
            # If there is no next person in line, return "NO"
            else:
                return "NO"

    # If all people have an even number of loaves, return the total number of loaves distributed
    return str(total_loaves)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()