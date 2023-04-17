#!/bin/python3

import math
import os
import random
import re
import sys

# document globals
N = None  # board size
B = None  # board in 0/1 (is prime?)
G = None  # grundy
RINT = None  # rows in B as Int
CINT = None  # columns in B as Int


#
# Complete the 'squareBoard' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY board as parameter.
#
def squareBoard(board):
    analyze(board)
    return 'First' if G[0][N - 1][0][N - 1] else 'Second'


def analyze(board):
    global N, B, G, RINT, CINT
    N = len(board)
    primes = {2, 3, 5, 7}
    B = [[int(n not in primes) for n in row] for row in board]
    RINT = [int(''.join(str(d) for d in reversed(row)), 2) for row in B]
    CINT = [int(''.join(str(d) for d in reversed(row)), 2) for row in zip(*B)]
    G = [[[[0] * N for i2 in range(N)] for i3 in range(N)] for i4 in range(N)]
    GT = [[[[0] * N for i2 in range(N)] for i3 in range(N)] for i4 in range(N)]
    if not any(rint for rint in RINT):
        G[0][N - 1][0][N - 1] = 0
        return
    # fill in grundy numbers for all rectangles [rlo,rhi] x [clo,chi]
    # grundy is ...
    #   0 if rectangle is size 1 or doesn't contain any nonprime,
    #   else mex of all (cut into two pieces and xor them)
    for rsize in range(1, N + 1):
        for csize in range(1, N + 1):
            if rsize == 1 == csize: continue
            for rlo in range(N - rsize + 1):
                rhi = rlo + rsize - 1
                for clo in range(N - csize + 1):
                    chi = clo + csize - 1
                    # look for nonprime
                    if rsize < csize:
                        mask = get_mask(clo, chi)
                        if not any(RINT[ri] & mask for ri in range(rlo, rhi + 1)):
                            continue
                    else:
                        mask = get_mask(rlo, rhi)
                        if not any(CINT[ci] & mask for ci in range(clo, chi + 1)):
                            continue
                    # okay, there is some nonprime, so must do cuts ...
                    grundy = [0] * 40
                    #   ... by row [rlo,rcut] + [rcut+1,rhi]
                    GT_slice = GT[clo][chi]
                    for rcut in range(rlo, rhi):
                        grundy[GT_slice[rlo][rcut] ^ GT_slice[rcut + 1][rhi]] = 1
                    #   ... by col [clo,ccut] + [ccut+1,chi]
                    G_slice = G[rlo][rhi]
                    for ccut in range(clo, chi):
                        grundy[G_slice[clo][ccut] ^ G_slice[ccut + 1][chi]] = 1
                    mex = grundy.index(0)
                    G_slice[clo][chi] = mex
                    GT_slice[rlo][rhi] = mex


def get_mask(i, j):
    return (1 << j + 1) - (1 << i)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        board = []

        for _ in range(n):
            board.append(list(map(int, input().rstrip().split())))

        result = squareBoard(board)

        fptr.write(result + '\n')

    fptr.close()