import random


def next_move(player, board):
    # Check if there is a winning move for the player
    for i in range(3):
        if board[i].count(player) == 2 and board[i].count('_') == 1:
            return i, board[i].index('_')
        col = [board[j][i] for j in range(3)]
        if col.count(player) == 2 and col.count('_') == 1:
            return col.index('_'), i
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]
    if diag1.count(player) == 2 and diag1.count('_') == 1:
        return diag1.index('_'), diag1.index('_')
    if diag2.count(player) == 2 and diag2.count('_') == 1:
        return diag2.index('_'), 2 - diag2.index('_')

    # If there is no winning move for the player, then block the opponent's winning moves
    opponent = 'O' if player == 'X' else 'X'
    for i in range(3):
        if board[i].count(opponent) == 2 and board[i].count('_') == 1:
            return i, board[i].index('_')
        col = [board[j][i] for j in range(3)]
        if col.count(opponent) == 2 and col.count('_') == 1:
            return col.index('_'), i
    if diag1.count(opponent) == 2 and diag1.count('_') == 1:
        return diag1.index('_'), diag1.index('_')
    if diag2.count(opponent) == 2 and diag2.count('_') == 1:
        return diag2.index('_'), 2 - diag2.index('_')

    # If there are no winning moves or opponent's winning moves, then choose a random empty cell
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                empty_cells.append((i, j))
    return random.choice(empty_cells)


def next_move(player, board):
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                empty_cells.append((i, j))

    if set(corners).issubset(empty_cells):
        return random.choice(corners)

    if board[1][1] == '_':
        return 1, 1

    if player == 'X' and board[0][0] == 'O' and board[2][2] == '_':
        return 2, 2
    elif player == 'X' and board[0][2] == 'O' and board[2][0] == '_':
        return 2, 0
    elif player == 'X' and board[2][0] == 'O' and board[0][2] == '_':
        return 0, 2
    elif player == 'X' and board[2][2] == 'O' and board[0][0] == '_':
        return 0, 0

    for i in range(3):
        if board[i].count(player) == 2 and board[i].count('_') == 1:
            return i, board[i].index('_')

    for j in range(3):
        col = [board[i][j] for i in range(3)]
        if col.count(player) == 2 and col.count('_') == 1:
            return col.index('_'), j

    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]
    if diag1.count(player) == 2 and diag1.count('_') == 1:
        return diag1.index('_'), diag1.index('_')
    if diag2.count(player) == 2 and diag2.count('_') == 1:
        return diag2.index('_'), 2 - diag2.index('_')

    opponent = 'O' if player == 'X' else 'X'
    for i in range(3):
        if board[i].count(opponent) == 2 and board[i].count('_') == 1:
            return i, board[i].index('_')

    for j in range(3):
        col = [board[i][j] for i in range(3)]
        if col.count(opponent) == 2 and col.count('_') == 1:
            return col.index('_'), j

    if diag1.count(opponent) == 2 and diag1.count('_') == 1:
        return diag1.index('_'), diag1.index('_')
    if diag2.count(opponent) == 2 and diag2.count('_') == 1:
        return diag2.index('_'), 2 - diag2.index('_')

    return random.choice(empty_cells)


if __name__ == '__main__':
    player = input().strip()
    board = [input().strip() for _ in range(3)]
    r, c = next_move(player, board)
    print(r, c)

