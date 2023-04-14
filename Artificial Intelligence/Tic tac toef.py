import random


def next_move(player, board):
    # Convert board to list of lists
    new_board = [list(row) for row in board]

    def get_empty_cells(board):
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    empty_cells.append((i, j))
        return empty_cells

    def check_win(board):
        # Check rows
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '_':
                return board[i][0]
        # Check columns
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != '_':
                return board[0][j]
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != '_':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != '_':
            return board[0][2]
        return None

    def minimax(board, depth, is_maximizing):
        result = check_win(board)
        if result is not None:
            if result == player:
                return 10 - depth
            else:
                return depth - 10
        elif len(get_empty_cells(board)) == 0:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i, j in get_empty_cells(board):
                board[i][j] = player
                score = minimax(board, depth + 1, False)
                board[i][j] = '_'
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i, j in get_empty_cells(board):
                board[i][j] = 'O' if player == 'X' else 'X'
                score = minimax(board, depth + 1, True)
                board[i][j] = '_'
                best_score = min(best_score, score)
            return best_score

    # Check if any winning move is available
    for i in range(3):
        for j in range(3):
            if new_board[i][j] == '_':
                new_board[i][j] = player
                if check_win(new_board) == player:
                    return i, j
                new_board[i][j] = '_'

    # Use minimax to select best move
    best_score = -float('inf')
    best_move = None
    for i, j in get_empty_cells(new_board):
        new_board[i][j] = player
        score = minimax(new_board, 0, False)
        new_board[i][j] = '_'
        if score > best_score:
            best_score = score
            best_move = (i, j)

    return best_move


if __name__ == '__main__':
    player = input().strip()
    board = [input().strip() for _ in range(3)]
    r, c = next_move(player, board)
    print(r, c)