def next_move(posr, posc, board):
    # Check if the current cell is dirty
    if board[posr][posc] == 'd':
        print("CLEAN")
        return

    # Calculate the distance of all dirty cells from the current position
    dirty_cells = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                distance = abs(posr-i) + abs(posc-j)
                dirty_cells.append((distance, i, j))

    # Move the bot to the closest dirty cell
    dirty_cells.sort()
    next_posr, next_posc = dirty_cells[0][1], dirty_cells[0][2]
    if next_posc < posc:
        print("LEFT")
    elif next_posc > posc:
        print("RIGHT")
    elif next_posr < posr:
        print("UP")
    elif next_posr > posr:
        print("DOWN")

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)