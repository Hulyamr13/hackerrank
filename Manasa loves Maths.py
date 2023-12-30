#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING n as parameter.
#

def solve(n):
    # Write your code here
    if len(n) < 3:
        if int(n) % 8 == 0:
            return "YES"
        elif int(n[::-1]) % 8 == 0:
            return "YES"
        else:
            return "NO"
    else:
        digits = [0] * 10
        for digit in n:
            digits[int(digit)] += 1

        for i in range(104, 1001, 8):
            original_digits = [0] * 10
            for digit in str(i):
                original_digits[int(digit)] += 1

            possible = True
            for j in range(10):
                if original_digits[j] > digits[j]:
                    possible = False
                    break

            if possible:
                return "YES"

        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = input()

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
