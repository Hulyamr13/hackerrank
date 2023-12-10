#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    def calc_super_digit(p):
        if len(p) == 1:
            return int(p)

        digit_sum = sum(int(digit) for digit in p)
        return calc_super_digit(str(digit_sum))

    super_digit_single = calc_super_digit(n)
    super_digit_total = calc_super_digit(str(super_digit_single * k))
    return super_digit_total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
