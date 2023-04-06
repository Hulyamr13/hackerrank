import random

def next_move(player, board):
    # Check if current player can win horizontally
    for i in range(3):
        if board[i].count(player) == 2 and board[i].count('_') == 1:
            return i, board[i].index('_')

    # Check if current player can win vertically
    for j in range(3):
        col = [board[i][j] for i in range(3)]
        if col.count(player) == 2 and col.count('_') == 1:
            return col.index('_'), j

    # Check if current player can win diagonally
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2-i] for i in range(3)]
    if diag1.count(player) == 2 and diag1.count('_') == 1:
        return diag1.index('_'), diag1.index('_')
    if diag2.count(player) == 2 and diag2.count('_') == 1:
        return diag2.index('_'), 2-diag2.index('_')

    # Check if opponent can win horizontally
    opponent = 'O' if player == 'X' else 'X'
    for i in range(3):
        if board[i].count(opponent) == 2 and board[i].count('_') == 1:
            return i, board[i].index('_')

    # Check if opponent can win vertically
    for j in range(3):
        col = [board[i][j] for i in range(3)]
        if col.count(opponent) == 2 and col.count('_') == 1:
            return col.index('_'), j

    # Check if opponent can win diagonally
    if diag1.count(opponent) == 2 and diag1.count('_') == 1:
        return diag1.index('_'), diag1.index('_')
    if diag2.count(opponent) == 2 and diag2.count('_') == 1:
        return diag2.index('_'), 2-diag2.index('_')

    # If none of the above conditions hold, select a random empty cell
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                empty_cells.append((i, j))
    return random.choice(empty_cells)

if __name__ == '__main__':
    player = input().strip()
    board = [input().strip() for _ in range(3)]
    r, c = next_move(player, board)
    print(r, c)