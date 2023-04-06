import math


def nextMove(player, board):
    # Define the opponent's symbol
    opponent = 'O' if player == 'X' else 'X'

    # Define the utility function for the board
    def utility(board):
        # Check rows
        for row in board:
            if len(set(row)) == 1 and row[0] != '_':
                return 1 if row[0] == player else -1

        # Check columns
        for j in range(3):
            if len(set([board[i][j] for i in range(3)])) == 1 and board[0][j] != '_':
                return 1 if board[0][j] == player else -1

        # Check diagonals
        if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != '_':
            return 1 if board[0][0] == player else -1
        if len(set([board[i][2 - i] for i in range(3)])) == 1 and board[0][2] != '_':
            return 1 if board[0][2] == player else -1

        # No winner, return 0
        return 0

    # Define the recursive Minimax function
    def minimax(board, depth, is_maximizing_player):
        # Check if the game is over or the depth limit has been reached
        score = utility(board)
        if score != 0 or depth == 0:
            return score

        # If the maximizing player's turn
        if is_maximizing_player:
            max_eval = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        board[i][j] = player
                        eval = minimax(board, depth - 1, False)
                        board[i][j] = '_'
                        max_eval = max(max_eval, eval)
            return max_eval

        # If the minimizing player's turn
        else:
            min_eval = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        board[i][j] = opponent
                        eval = minimax(board, depth - 1, True)
                        board[i][j] = '_'
                        min_eval = min(min_eval, eval)
            return min_eval

    # Find the best move using Minimax
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                eval = minimax(board, 10, False)
                board[i][j] = '_'
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    # Make the best move
    if best_move:
        print(best_move[0], best_move[1])
    else:
        print("-1 -1")


if __name__ == '__main__':
    # Read input
    player = input().strip()
    board = [input().strip() for _ in range(3)]
    board = [list(row) for row in board]

    # Call nextMove function
    nextMove(player, board)
