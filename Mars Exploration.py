#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    changed = 0
    for i in range(0, len(s), 3):
        if s[i:i+3] != "SOS":
            for j in range(3):
                if i+j < len(s) and s[i+j] != "SOS"[j]:
                    changed += 1
    return changed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
