#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY y as parameter.
#

def solve(y):
    # Write your code here
    n = len(y)
    result = [(sum(1 for other_num in y if other_num >= num)) for num in y]
    V = sum((n + 1) / (result[i] + 1) for i in range(n))

    return ["{:.2f}".format(V)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        y_count = int(input().strip())

        y = list(map(int, input().rstrip().split()))

        result = solve(y)

        fptr.write('\n'.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
