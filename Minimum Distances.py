#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    min_dist = float('inf')  # set the initial minimum distance to infinity
    indices = {}  # dictionary to store indices of each element

    # loop through the array
    for i in range(len(a)):
        if a[i] in indices:  # if we have seen this element before
            dist = i - indices[a[i]]  # calculate the distance between the current index and the previous index
            min_dist = min(min_dist, dist)  # update the minimum distance if necessary
        indices[a[i]] = i  # store the current index of the element

    return min_dist if min_dist != float(
        'inf') else -1  # return the minimum distance, or -1 if no matching elements were found


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()