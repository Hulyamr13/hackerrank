#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

from collections import deque

def quickestWayUp(ladders, snakes):
    # Create an array to represent the game board
    board = [float('inf')] * 101  # 101 to make indexing easier

    # Populate the board with ladder and snake information
    for start, end in ladders:
        board[start] = end
    for start, end in snakes:
        board[start] = end

    # Start BFS from the starting square (square 1)
    queue = deque([(1, 0)])  # Tuple of (square, rolls)
    board[1] = 0  # Mark starting square as visited with 0 rolls

    while queue:
        square, rolls = queue.popleft()

        # Roll the die from 1 to 6
        for i in range(1, 7):
            next_square = square + i

            # If next square is beyond the board, skip
            if next_square > 100:
                continue

            # If next square is a ladder or snake, update next_square
            if board[next_square] != float('inf'):
                next_square = board[next_square]

            # If next square is not visited yet, update board and add to queue
            if board[next_square] == float('inf'):
                board[next_square] = rolls + 1
                queue.append((next_square, rolls + 1))

    # If destination square is not reached, return -1
    if board[100] == float('inf'):
        return -1
    else:
        return board[100]

# Test case from the problem statement
ladders = [[32, 62], [42, 68], [12, 98]]
snakes = [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
print(quickestWayUp(ladders, snakes))  # Output: 3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
