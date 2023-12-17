#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cubeSum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY operations
#

def cubeSum(n, operations):
    # Write your code here
    data = {}
    results = []
    for op in operations:
        info = op.split()
        if info[0] == "UPDATE":
            data[info[1] + " " + info[2] + " " + info[3]] = int(info[4])
        else:
            x1 = int(info[1])
            y1 = int(info[2])
            z1 = int(info[3])
            x2 = int(info[4])
            y2 = int(info[5])
            z2 = int(info[6])
            res = 0
            for k, v in data.items():
                corr = [int(s) for s in k.split()]
                if corr[0] <= x2 and x1 <= corr[0] and corr[1] <= y2 and y1 <= corr[1] and corr[2] <= z2 and z1 <= corr[2]:
                    res += v
            results.append(res)
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        first_multiple_input = input().rstrip().split()

        matSize = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        ops = []

        for _ in range(m):
            ops_item = input()
            ops.append(ops_item)

        res = cubeSum(matSize, ops)

        fptr.write('\n'.join(map(str, res)))
        fptr.write('\n')

    fptr.close()
