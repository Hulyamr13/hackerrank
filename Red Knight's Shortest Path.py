import sys


def printShortestPath(n, i_start, j_start, i_end, j_end):
    #  Print the distance along with the sequence of moves.
    diff_i = i_end - i_start
    diff_j = j_end - j_start
    i = i_start
    j = j_start
    if diff_i % 2 == 1:
        print('Impossible')
        return
    if diff_i % 4 == 0 and diff_j % 2 == 1:
        print('Impossible')
        return
    if diff_i % 4 == 2 and diff_j % 2 == 0:
        print('Impossible')
        return
    moves = []
    while diff_i < 0 and diff_i // -2 > diff_j:
        if j == 0:
            diff_i += 2
            diff_j -= 1
            i -= 2
            j += 1
            moves.append('UR')
            continue
        diff_i += 2
        diff_j += 1
        i -= 2
        j -= 1
        moves.append('UL')
    while diff_i < 0:
        diff_i += 2
        diff_j -= 1
        i -= 2
        j += 1
        moves.append('UR')
    while diff_j > 0 and diff_j > diff_i // 2:
        moves.append('R')
        j += 2
        diff_j -= 2
    while diff_i > 0 and diff_i // -2 < diff_j:
        if j == n - 1:
            diff_i -= 2
            diff_j += 1
            i += 2
            j -= 1
            moves.append('LL')
            continue
        moves.append('LR')
        diff_i -= 2
        diff_j -= 1
        i += 2
        j += 1
    while diff_i > 0:
        diff_i -= 2
        diff_j += 1
        i += 2
        j -= 1
        moves.append('LL')

    if diff_i == 0:
        if diff_j > 0:
            move = diff_j // 2
            moves += ["R"] * move
        else:
            move = -diff_j // 2
            moves += ["L"] * move

    print(len(moves))
    print(' '.join(moves))


if __name__ == "__main__":
    n = int(input().strip())
    i_start, j_start, i_end, j_end = input().strip().split(' ')
    i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end), int(j_end)]
    printShortestPath(n, i_start, j_start, i_end, j_end)