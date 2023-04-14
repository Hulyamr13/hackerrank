import random


def next_move(player, board):
    # Convert board to list of lists
    new_board = [list(row) for row in board]

    # Define center, edges, and corners
    center = (1, 1)
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]

    # Check if there's a winning move
    for i in range(3):
        if new_board[i].count(player) == 2 and new_board[i].count('_') == 1:
            return i, new_board[i].index('_')

        col = [new_board[j][i] for j in range(3)]
        if col.count(player) == 2 and col.count('_') == 1:
            return col.index('_'), i

    diag1 = [new_board[i][i] for i in range(3)]
    diag2 = [new_board[i][2 - i] for i in range(3)]
    if diag1.count(player) == 2 and diag1.count('_') == 1:
        return diag1.index('_'), diag1.index('_')
    if diag2.count(player) == 2 and diag2.count('_') == 1:
        return diag2.index('_'), 2 - diag2.index('_')

    # Check if there's a counter-attack move
    for i in range(3):
        if new_board[i].count(player) == 1 and new_board[i].count('_') == 2:
            return i, new_board[i].index('_')

        col = [new_board[j][i] for j in range(3)]
        if col.count(player) == 1 and col.count('_') == 2:
            return col.index('_'), i

    if diag1.count(player) == 1 and diag1.count('_') == 2:
        return diag1.index('_'), diag1.index('_')
    if diag2.count(player) == 1 and diag2.count('_') == 2:
        return diag2.index('_'), 2 - diag2.index('_')

    # Check if the center is free
    if new_board[1][1] == '_':
        return center

    # Check if there's an edge move to make
    for i, j in edges:
        if new_board[i][j] == '_':
            return i, j

    # Check if there's a corner move to make
    for i, j in corners:
        if new_board[i][j] == '_':
            return i, j

    # If all else fails, make a random move
    empty_cells = [(i, j) for i in range(3) for j in range(3) if new_board[i][j] == '_']
    return random.choice(empty_cells)


if __name__ == '__main__':
    player = input().strip()
    board = [input().strip() for _ in range(3)]
    r, c = next_move(player, board)
    print(r, c)