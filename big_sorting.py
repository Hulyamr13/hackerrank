#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bigSorting function below.
def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))
    # temp = list(map(str, temp))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()