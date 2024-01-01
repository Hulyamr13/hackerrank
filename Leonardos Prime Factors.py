#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def primeCount(n):
    x = 0
    s = 1
    for i in range(2, n+1):
        flag = True
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            s *= i
            if s > n:
                break
            x += 1
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
