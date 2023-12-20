#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    chars = set(s)
    max_len = 0

    for c1 in chars:
        for c2 in chars:
            if c1 == c2:
                continue

            temp = [x for x in s if x == c1 or x == c2]

            alternating = True
            for i in range(len(temp) - 1):
                if temp[i] == temp[i + 1]:
                    alternating = False
                    break

            if alternating:
                max_len = max(max_len, len(temp))

    return max_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
