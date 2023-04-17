import random

board = []
moves = ["UP", "DOWN", "LEFT", "RIGHT"]
valid_moves = []
i_x, i_y, o_x, o_y = 0, 0, 0, 0
player = input()
i_x, i_y, o_x, o_y = map(int, input().split())
for _ in range(15):
    row = input().strip()
    board.append(row)

if player == "r":
    x, y = i_x, i_y
else:
    x, y = o_x, o_y

for i in range(-1, 2):
    for j in range(-1, 2):
        if (i == 0 and j != 0) or (i != 0 and j == 0):
            new_x, new_y = x + i, y + j
            if 0 <= new_x < 15 and 0 <= new_y < 15 and board[new_x][new_y] == "-":
                if i == -1:
                    valid_moves.append(0)
                elif i == 1:
                    valid_moves.append(1)
                elif j == -1:
                    valid_moves.append(2)
                elif j == 1:
                    valid_moves.append(3)

if valid_moves:
    random_move = random.choice(valid_moves)
    print(moves[random_move])
else:
    random_move = random.randint(0, 3)
    print(moves[random_move])