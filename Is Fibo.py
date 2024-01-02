#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isFibo' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def isFibo(n):
    # Write your code here
    first, second = 0, 1

    for i in range(n):
        temp = second
        second += first
        first = temp

        if second == n:
            return "IsFibo"
        if second > n:
            return "IsNotFibo"

    return "IsNotFibo"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = isFibo(n)

        fptr.write(result + '\n')

    fptr.close()
