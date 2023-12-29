from operator import mul


def matrixMult(m1, m2, d):
    m2tr = list(zip(*m2))
    return [[sum(map(mul, m1row, m2col)) % d for m2col in m2tr] for m1row in m1]


def matrixVectorMult(m, v):
    return [sum(map(mul, mrow, v)) for mrow in m]


def matrixPowMod(mat, p, d):
    dim = len(mat)
    cur = [[i == j and 1 or 0 for j in range(dim)] for i in range(dim)]
    for c in bin(p)[2:]:
        cur = matrixMult(cur, cur, d)
        if c == '1':
            cur = matrixMult(cur, mat, d)
    return cur


modulo = 10 ** 9
T = int(input().strip())
for _ in range(T):
    a, b, c, d, e, f, g, h, n = list(map(int, input().strip().split()))
    mat = [[0] * 22 for i in range(22)]
    mat[0][1] = mat[1][2] = mat[2][3] = mat[3][4] = mat[4][5] = mat[5][6] = mat[6][7] = mat[7][8] = 1
    mat[8][9 - a] += 1
    mat[8][20 - b] += 1
    mat[8][20 - c] += 1
    mat[8][9] = mat[8][10] = mat[9][9] = mat[9][10] = mat[10][10] = d
    mat[11][12] = mat[12][13] = mat[13][14] = mat[14][15] = mat[15][16] = mat[16][17] = mat[17][18] = mat[18][19] = 1
    mat[19][20 - e] += 1
    mat[19][9 - f] += 1
    mat[19][9 - g] += 1
    mat[19][20] = mat[19][21] = mat[20][20] = mat[20][21] = mat[21][21] = h
    vec = [1] * 22
    vec[8] = vec[19] = 3
    vec[9] = vec[20] = 0
    resultVec = matrixVectorMult(matrixPowMod(mat, n, modulo), vec)
    print(resultVec[8] % modulo, resultVec[19] % modulo)
