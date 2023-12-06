#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'divisibleNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def divisibleNumbers(n):
    # Write your code here
    i = n
    while True:
        digits_sum = sum(int(d) for d in str(i))
        digits_product = 1
        for d in str(i):
            if d == '0':
                break
            digits_product *= int(d)
        if digits_sum >= digits_product and n % i == 0:
            return len(str(i))
        i += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = divisibleNumbers(n)

    fptr.write(str(result) + '\n')

    fptr.close()
