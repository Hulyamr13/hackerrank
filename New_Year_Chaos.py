#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    q = [p - 1 for p in q]  # Convert to 0-indexed positions

    for i, person in enumerate(q):
        if person - i > 2:
            print("Too chaotic")
            return

        # Count the number of people who bribed the current person
        for j in range(max(0, person - 1), i):
            if q[j] > person:
                bribes += 1

    print(bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
