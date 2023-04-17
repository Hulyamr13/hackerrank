import os

def isprime(d):
    return d == 2 or d == 3 or d == 5 or d == 7

def getSG(i, j, k, l, SG, pl):
    x, SGT = 0, [0] * 70

    if SG[i][j][k][l] != -1:
        return SG[i][j][k][l]

    if not pl[i][j][k][l]:
        SG[i][j][k][l] = 0
        return 0

    for x in range(i, k):
        SGT[getSG(i, j, x, l, SG, pl) ^ getSG(x + 1, j, k, l, SG, pl)] = 1

    for x in range(j, l):
        SGT[getSG(i, j, k, x, SG, pl) ^ getSG(i, x + 1, k, l, SG, pl)] = 1

    while SGT[x] != 0:
        x += 1

    SG[i][j][k][l] = x
    return x

def squareBoard(board):
    n = len(board)
    SG, pl = [[[[ -1 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)], \
            [[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            pl[i][j][i][j] = not isprime(board[i][j])

    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    if k > i and pl[i][j][k-1][l]:
                        pl[i][j][k][l] = 1
                    if l > j and pl[i][j][k][l-1]:
                        pl[i][j][k][l] = 1
                    if not isprime(board[k][l]):
                        pl[i][j][k][l] = 1

    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    SG[i][j][k][l] = getSG(i, j, k, l, SG, pl)

    return "Second" if SG[0][0][n-1][n-1] == 0 else "First"

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