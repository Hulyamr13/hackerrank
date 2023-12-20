#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#
import copy


def bomberMan(n, grid):
    # Write your code here
    def printans(g):
        for val in g:
            print("".join(val))

    save = []
    timer = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        grid[i] = list(grid[i])

    save.append(copy.deepcopy(grid))
    save.append(copy.deepcopy(grid))

    sec = 1
    for t in range(1, 5):
        sec = sec + 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 'O':
                    grid[i][j] = 'O'
                    timer[i][j] = sec

        save.append(copy.deepcopy(grid))

        dx = [+0, +0, +1, -1]
        dy = [+1, -1, +0, +0]
        g2 = copy.deepcopy(grid)

        sec = sec + 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O' and timer[i][j] == sec - 3:
                    g2[i][j] = '.'
                    for k in range(4):
                        di = i + dx[k]
                        dj = j + dy[k]
                        if 0 <= di < len(grid) and 0 <= dj < len(grid[0]):
                            g2[di][dj] = '.'

        grid = copy.deepcopy(g2)
        save.append(copy.deepcopy(grid))

    result = []
    if n == 1:
        result = save[n]
    elif n % 2 == 0:
        result = save[2]
    elif n % 4 == 1:
        result = save[5]
    elif n % 4 == 3:
        result = save[3]

    ans = []
    for val in result:
        ans.append("".join(val))

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
