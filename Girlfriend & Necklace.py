# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def testcases(cin=sys.stdin):
    t = int(cin.readline())
    for _ in range(t):
        yield int(cin.readline())

MOD = int(1e9 + 7)
MAT = [[1, 0, 1], [1, 0, 0], [0, 1, 0]]

def num_necklaces(n):
    z = mod_power(MAT, n-2)
    return sum(v for r in z for v in r) % MOD

def mod_power(mat, e):
    s = len(mat)
    r = [[0]*s for _ in range(s)]
    for i in range(s):
        r[i][i] = 1

    while e:
        if e & 1:
            r = mat_mult(s, r, mat)
        e >>= 1
        mat = mat_mult(s, mat, mat)
    return r

def mat_mult(s, a, b):
    r = [[0]*s for _ in range(s)]

    for i in range(s):
        for j in range(s):
            for k in range(s):
                r[i][j] += a[i][k] * b[k][j]
            r[i][j] %= MOD

    return r

for n in testcases():
    result = num_necklaces(n)
    print(result)
