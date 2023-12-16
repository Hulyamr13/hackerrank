#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x.sort()

    # Initialize a list to keep track of houses with transmitters
    transmitter_houses = [0] * 100001

    # Mark houses with transmitters
    for i in x:
        transmitter_houses[i - 1] = 1

    # Create a new list with houses having transmitters
    transmitter_positions = []
    for i in range(100001):
        if transmitter_houses[i] == 1:
            transmitter_positions.append(i + 1)

    start = 0
    i = 0
    count = 1
    n = len(transmitter_positions)

    # Calculate the minimum number of transmitters required
    while i < n:
        if transmitter_positions[i] <= transmitter_positions[start] + k:
            i += 1
            continue
        else:
            s = i - 1
            while i < n and transmitter_positions[s] + k >= transmitter_positions[i]:
                i += 1
            start = i
            if i < n:
                count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
