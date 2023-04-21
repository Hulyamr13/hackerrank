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
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False for _ in range(m)] for _ in range(n)] # To keep track of visited cells
    max_region = 0 # To store the size of the largest region

    # Helper function to perform depth-first search (DFS)
    def dfs(row, col):
        if row < 0 or row >= n or col < 0 or col >= m: # Check if the cell is within the matrix boundaries
            return 0
        if visited[row][col]: # If the cell is already visited, return 0
            return 0
        visited[row][col] = True # Mark the cell as visited
        if matrix[row][col] == 0: # If the cell is not a filled cell, return 0
            return 0
        size = 1 # Initialize the size of the current region with 1 (for the current cell)
        # Perform DFS recursively on all neighboring cells (horizontally, vertically, diagonally)
        size += dfs(row-1, col)
        size += dfs(row+1, col)
        size += dfs(row, col-1)
        size += dfs(row, col+1)
        size += dfs(row-1, col-1)
        size += dfs(row-1, col+1)
        size += dfs(row+1, col-1)
        size += dfs(row+1, col+1)
        return size

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]: # If the cell is a filled cell and not visited
                region_size = dfs(i, j) # Perform DFS on the current cell to find the size of the region
                max_region = max(max_region, region_size) # Update the size of the largest region

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