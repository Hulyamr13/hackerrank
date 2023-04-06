import math
import random


def nextMove(player, board):
    opponent = "O" if player == "X" else "X"

    def evaluate(board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '_':
                return 10 if board[i][0] == player else -10
            if board[0][i] == board[1][i] == board[2][i] != '_':
                return 10 if board[0][i] == player else -10
        if board[0][0] == board[1][1] == board[2][2] != '_':
            return 10 if board[0][0] == player else -10
        if board[0][2] == board[1][1] == board[2][0] != '_':
            return 10 if board[0][2] == player else -10
        return 0

    def minimax(board, depth, is_maximizing_player, alpha, beta):
        score = evaluate(board)
        if score != 0:
            return score

        if depth == 0:
            return 0

        if is_maximizing_player:
            max_eval = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        board[i][j] = player
                        eval = minimax(board, depth - 1, False, alpha, beta)
                        board[i][j] = '_'
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        board[i][j] = opponent
                        eval = minimax(board, depth - 1, True, alpha, beta)
                        board[i][j] = '_'
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def random_move(board):
        empty_spots = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    empty_spots.append((i, j))
        return random.choice(empty_spots)

    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                score = minimax(board, 2, False, -math.inf, math.inf)
                board[i][j] = '_'
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move


player = input().strip()
board = [list(input().strip()) for _ in range(3)]
move = nextMove(player, board)
print(move[0], move[1])
