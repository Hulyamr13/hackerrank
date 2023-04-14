def nextMove(posr, posc, board):
    # Calculate distance to each dirty cell
    dirty_cells = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'd':
                distance = abs(posr - i) + abs(posc - j)
                dirty_cells.append(((i, j), distance))

    # Sort the dirty cells by distance in ascending order
    dirty_cells.sort(key=lambda x: x[1])

    # Move towards the nearest dirty cell
    if dirty_cells:
        nearest_dirty_cell = dirty_cells[0][0]
        if nearest_dirty_cell[1] < posc:
            print('LEFT')
        elif nearest_dirty_cell[1] > posc:
            print('RIGHT')
        elif nearest_dirty_cell[0] < posr:
            print('UP')
        elif nearest_dirty_cell[0] > posr:
            print('DOWN')
        else:
            print('CLEAN')
    else:
        print('CLEAN')

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)