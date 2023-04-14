def find_nearest_dirty(posx, posy, dimx, dimy, board):
    min_dist = float('inf')
    dirty_pos = None
    for i in range(dimx):
        for j in range(dimy):
            if board[i][j] == 'd':
                dist = abs(posx - i) + abs(posy - j)
                if dist < min_dist:
                    min_dist = dist
                    dirty_pos = (i, j)
    return dirty_pos

def next_move(posx, posy, dimx, dimy, board):
    dirty_pos = find_nearest_dirty(posx, posy, dimx, dimy, board)
    if dirty_pos:
        dx, dy = dirty_pos
        if posx > dx:
            print("UP")
        elif posx < dx:
            print("DOWN")
        elif posy > dy:
            print("LEFT")
        elif posy < dy:
            print("RIGHT")
        else:
            print("CLEAN")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
