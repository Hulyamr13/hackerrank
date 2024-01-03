#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER x as parameter.
#

def find_number(t):
    for _ in range(t):
        n = int(input())
        count_of_two = 0
        count_of_five = 0

        while n % 2 == 0:
            n = n >> 1
            count_of_two += 1

        while n % 5 == 0:
            n //= 5
            count_of_five += 1

        j = max(count_of_two - 2, count_of_five)
        count = 1
        a = 1

        while a % n != 0:
            a = (a * 10 + 1) % n
            count += 1

        print(2 * count + j)


if __name__ == "__main__":
    t = int(input())
    find_number(t)
