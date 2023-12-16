#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    # Write your code here
    x = 0
    for i in s:
        x ^= i

    if len(set(s)) == 1 and 1 in s:
        if x:
            return "Second"
        else:
            return "First"
    else:
        if x:
            return "First"
        else:
            return "Second"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
