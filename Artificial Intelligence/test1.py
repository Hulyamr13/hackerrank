import math
import os
import random
import re
import sys

def nextMove(player, board):
    # Check if we can win in the next move horizontally
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == '_':
            return i, 2
        elif board[i][0] == player and board[i][2] == player and board[i][1] == '_':
            return i, 1
        elif board[i][1] == player and board[i][2] == player and board[i][0] == '_':
            return i, 0

    # Check if we can win in the next move vertically
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == '_':
            return 2, j
        elif board[0][j] == player and board[2][j] == player and board[1][j] == '_':
            return 1, j
        elif board[1][j] == player and board[2][j] == player and board[0][j] == '_':
            return 0, j

    # Check if we can win in the next move diagonally
    if board[0][0] == player and board[1][1] == player and board[2][2] == '_':
        return 2, 2
    elif board[0][0] == player and board[2][2] == player and board[1][1] == '_':
        return 1, 1
    elif board[1][1] == player and board[2][2] == player and board[0][0] == '_':
        return 0, 0
    elif board[0][2] == player and board[1][1] == player and board[2][0] == '_':
        return 2, 0
    elif board[0][2] == player and board[2][0] == player and board[1][1] == '_':
        return 1, 1
    elif board[1][1] == player and board[2][0] == player and board[0][2] == '_':
        return 0, 2

    # Check if opponent can win in the next move horizontally
    for i in range(3):
        if board[i][0] != '_' and board[i][0] != player and board[i][0] == board[i][1] and board[i][2] == '_':
            return i, 2
        elif board[i][0] != '_' and board[i][0] != player and board[i][2] == board[i][0] and board[i][1] == '_':
            return i, 1
        elif board[i][1] != '_' and board[i][1] != player and board[i][2] == board[i][1] and board[i][0] == '_':
            return i, 0

    # Check if opponent can win in the next move vertically
    for j in range(3):
        if board[0][j] != '_' and board[0][j] != player and board[0][j] == board[1][j] and board[2][j] == '_':
            return 2, j
        elif board[0][j] != '_' and board[0][j] != player and board[2][j] == board[0][j] and board[1][j] == '':
            return 1, j
        elif board[1][j] != '' and board[1][j] != player and board[1][j] == board[2][j] and board[0][j] == '_':
            return 0, j
    # Check if opponent can win in the next move diagonally
    if board[0][0] != '_' and board[0][0] != player and board[0][0] == board[1][1] and board[2][2] == '_':
        return 2, 2
    elif board[0][0] != '_' and board[0][0] != player and board[2][2] == board[0][0] and board[1][1] == '_':
        return 1, 1
    elif board[1][1] != '_' and board[1][1] != player and board[2][2] == board[1][1] and board[0][0] == '_':
        return 0, 0
    elif board[0][2] != '_' and board[0][2] != player and board[1][1] == board[0][2] and board[2][0] == '_':
        return 2, 0
    elif board[0][2] != '_' and board[0][2] != player and board[2][0] == board[0][2] and board[1][1] == '_':
        return 1, 1
    elif board[1][1] != '_' and board[1][1] != player and board[2][0] == board[1][1] and board[0][2] == '_':
        return 0, 2

    # If none of the above conditions hold, select a random empty cell
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                empty_cells.append((i, j))
    return random.choice(empty_cells)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])

    s = first_multiple_input[1]

    board = []
    for i in range(3):
        row = input().strip()
        board.append([c for c in row])
        r, c = nextMove('X', board)
        print(r, c)
