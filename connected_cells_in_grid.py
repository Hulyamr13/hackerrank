#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    # Write your code here
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_region = 0

    def dfs(row, col):
        if row < 0 or row >= n or col < 0 or col >= m:
            return 0
        if visited[row][col]:
            return 0
        visited[row][col] = True
        if matrix[row][col] == 0:
            return 0
        size = 1

        size += dfs(row - 1, col)
        size += dfs(row + 1, col)
        size += dfs(row, col - 1)
        size += dfs(row, col + 1)
        size += dfs(row - 1, col - 1)
        size += dfs(row - 1, col + 1)
        size += dfs(row + 1, col - 1)
        size += dfs(row + 1, col + 1)
        return size

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                region_size = dfs(i, j)
                max_region = max(max_region, region_size)

    return max_region


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
