#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    n = len(petrolpumps)
    start, tank = 0, 0

    for i in range(n):
        start = i
        tank = 0

        for j in range(n):
            current = (start + j) % n
            tank += petrolpumps[current][0] - petrolpumps[current][1]

            if tank < 0:
                break

            if j == n - 1:
                return start


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
