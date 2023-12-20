#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    curSum = -sys.maxsize
    maxSum = -sys.maxsize
    m1 = -sys.maxsize
    posNums = 0

    for num in arr:

        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

        if num > 0:
            posNums += num
        elif num >= m1:
            m1 = num

    if posNums == 0:
        return [maxSum, m1]
    else:
        return [maxSum, posNums]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
