#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    total = len(arr)
    positive = sum(1 for i in arr if i > 0)
    negative = sum(1 for i in arr if i < 0)
    zero = sum(1 for i in arr if i == 0)

    print(f"{positive / total:.6f}")
    print(f"{negative / total:.6f}")
    print(f"{zero / total:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
