import random

board = []
moves = ["UP", "DOWN", "LEFT", "RIGHT"]
valid_moves = []

player, i_x, i_y, o_x, o_y = input().split()
i_x, i_y, o_x, o_y = int(i_x), int(i_y), int(o_x), int(o_y)

x, y = (i_x, i_y) if player == "r" else (o_x, o_y)

for i in range(15):
    board.append(input())

for i in range(-1, 2):
    for j in range(-1, 2):
        if (i == 0 and j != 0) or (i != 0 and j == 0):
            if board[x+i][y+j] == "-":
                if i == -1:
                    valid_moves.append(0)
                if i == 1:
                    valid_moves.append(1)
                if j == -1:
                    valid_moves.append(2)
                if j == 1:
                    valid_moves.append(3)

if len(valid_moves) != 0:
    random_index = random.randint(0, len(valid_moves)-1)
    print(moves[valid_moves[random_index]])
else:
    print(moves[random.randint(0, len(moves)-1)])