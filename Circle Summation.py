def rot_vec(array, k, sign):
    """Rotate a vector's entries some amount right (sign = +1) or left (sign = -1)"""
    if sign == 1:
        return array[len(array)-k:] + array[0:len(array)-k]
    elif sign == -1:
        return array[k:] + array[0:k]

def unit_mat(n):
    mat = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        mat[i][i] = 1
    return mat

def mat_mult(A, B):
    """Multiply two matrices. Currently assumes the dimensions match up."""
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(C)):
        for j in range(len(C[0])):
            C[i][j] = sum([A[i][k]*B[k][j] for k in range(len(B))]) % 1000000007
    return C

def display(v):
    print(" ".join(map(lambda x: str(x[0]), v)))


### the main loop

T = int(input().strip())

for t in range(0, T):
    N, M = map(int, input().strip().split(" "))
    a = list(map(lambda x: [int(x)], input().strip().split(" ")))

    """ Construct the "once-around" transition matrix """
    cyc = unit_mat(N)

    cyc[0][1] = 1
    cyc[0][N-1] = 1  # Handle the first row
    for i in range(1, N-1):  # Handle the middle rows
        for j in range(N):
            cyc[i][j] += cyc[i-1][j] + cyc[i+1][j]
    for j in range(N):
        cyc[N-1][j] += cyc[N-2][j] + cyc[0][j]

    """ Iterate the procedure """
    reps = M // N
    rem = M % N
    pows = list(map(int, list(bin(reps)[2:])))
    pows.reverse()

    # First, handle all the cycles
    accum = unit_mat(N)

    if pows[0] == 1:
        accum = mat_mult(cyc, accum)

    for p in pows[1:]:
        cyc = mat_mult(cyc, cyc)
        if p == 1:
            accum = mat_mult(cyc, accum)

    # Then handle the remainder
    if rem > 0:
        for j in range(N):
            accum[0][j] += accum[N-1][j] + accum[1][j]
        for i in range(1, rem):
            for j in range(N):
                accum[i][j] += accum[i-1][j] + accum[i+1][j]

    for i in range(N):
        display(rot_vec(mat_mult(accum, rot_vec(a, i, -1)), i, 1))
    if t < T-1:
        print("")
