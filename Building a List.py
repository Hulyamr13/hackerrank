#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING s as parameter.
#

def compute(prev, curr):
    for i in range(len(curr)):
        t = prev + curr[i]
        print(t)
        compute(t, curr[i + 1:])


if __name__ == "__main__":
    test_num = int(input())

    for _ in range(test_num):
        size = int(input())
        curr = input()
        curr = ''.join(sorted(curr))
        compute("", curr)