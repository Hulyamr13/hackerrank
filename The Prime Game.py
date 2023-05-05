#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'winner' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

# 2, 3, 5, 7, 11, 13
values = [0, 0, 1, 1, 2, 2, 3, 3, 4]


def winner(A):
    nimber = 0  # or grundy number
    for ak in A:
        nimber ^= values[ak % len(values)]

    return "Manasa" if nimber > 0 else "Sandy"


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = winner(A)

        print(result)