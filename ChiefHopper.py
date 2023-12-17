#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def chiefHopper(arr):
    # Write your code here
    high = low = 0

    for i in arr:
        if i > high:
            high = i
        if i < low:
            low = i

    def tester(x, arr):
        energy = x
        for height in arr:
            if height > energy:
                energy -= (height - energy)
                if energy < 0:
                    return False
            else:
                energy += (energy - height)
        return True

    cont = True
    i = (high + low) // 2
    dic = {}

    while cont:
        if dic.get(i - 1, tester(i - 1, arr)):
            high = i
            i = (high + low) // 2
        else:
            if dic.get(i, tester(i, arr)):
                cont = False
            else:
                low = i
                i = ((i + high + 1) // 2)
                if i == 0:
                    i = 1

    return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
