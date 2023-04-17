#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    lcm_a = 1
    for num in a:
        lcm_a = lcm_a * num // math.gcd(lcm_a, num)

    gcd_b = b[0]
    for num in b[1:]:
        gcd_b = math.gcd(gcd_b, num)

    count = 0
    for factor in range(lcm_a, gcd_b + 1, lcm_a):
        if all(factor % num == 0 for num in a) and all(num % factor == 0 for num in b):
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()