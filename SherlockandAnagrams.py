#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from collections import Counter


def all_substrs(s):
    return [[s[j:j + i] for j in range(len(s) - i + 1)] for i in range(1, len(s))]


def countem(ll):
    c = Counter()
    s = 0
    for lst in ll:
        for e in lst:
            q = ''.join(sorted(e))
            c[q] += 1
    for e in c:
        s += int(c[e] * (c[e] - 1) / 2)
    return s


def sherlockAndAnagrams(s):
    # Write your code here
    substrings = all_substrs(s)
    return countem(substrings)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
