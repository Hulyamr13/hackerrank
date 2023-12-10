#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringReduction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringReduction(s):
    char_count = {'a': 0, 'b': 0, 'c': 0}
    for i in s:
        char_count[i] += 1
    if char_count['a'] % 2 == char_count['b'] % 2 == char_count['c'] % 2:
        return 2
    elif len(set(s)) == 1:
        return len(s)
    else:
        return 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringReduction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
