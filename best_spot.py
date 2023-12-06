#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bestSpot' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY heights
#  2. 2D_INTEGER_ARRAY store
#

def bestSpot(heights, store):
    # Write your code here
    R, C = len(heights), len(heights[0])
    H, W = len(store), len(store[0])

    min_diff = float('inf')
    best_i, best_j = -1, -1

    for i in range(R - H + 1):
        for j in range(C - W + 1):
            diff = 0
            for x in range(H):
                for y in range(W):
                    diff += (store[x][y] - heights[i + x][j + y]) ** 2

            if diff < min_diff:
                min_diff = diff
                best_i, best_j = i + 1, j + 1

    print(min_diff)
    print(best_i, best_j)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    heights = []

    for _ in range(r):
        heights.append(list(map(int, input().rstrip().split())))

    second_multiple_input = input().rstrip().split()

    h = int(second_multiple_input[0])

    w = int(second_multiple_input[1])

    store = []

    for _ in range(h):
        store.append(list(map(int, input().rstrip().split())))

    bestSpot(heights, store)
