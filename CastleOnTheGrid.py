#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    from collections import deque

    # Create a namedtuple for points
    class point(tuple):
        def __add__(self, other):
            return point(x + y for x, y in zip(self, other))

    # Define possible movements
    movements = [point((0, -1)), point((-1, 0)), point((0, 1)), point((1, 0))]

    # Convert grid to list
    grid = [list(row) for row in grid]

    # Initialize start and goal points
    start = point((startX, startY))
    goal = point((goalX, goalY))

    # Mark start and goal points in the grid
    grid[startX][startY] = 's'
    grid[goalX][goalY] = 'g'

    # Initialize visited set and queue for BFS
    visited = set()
    queue = deque([(start, 0)])

    # Perform BFS
    while queue:
        current, moves = queue.popleft()
        if current == goal:
            return moves

        for move in movements:
            next_pos = current + move
            while 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0]) and grid[next_pos[0]][
                next_pos[1]] != 'X':
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
                next_pos += move

    return -1  # If no path found


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])
    startY = int(first_multiple_input[1])
    goalX = int(first_multiple_input[2])
    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
