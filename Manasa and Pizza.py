M = 10**9 + 7
O = M - 1

def ml(a, b):
    return [[(a[i][0] * b[0][j] + a[i][1] * b[1][j]) % M for j in range(2)] for i in range(2)]

def pw(m, N):
    r = [[1, 0], [0, 1]]
    while N:
        if N & 1:
            r = ml(r, m)
        if N:
            m = ml(m, m)
        N >>= 1
    return r

input()
A = lambda n: pw([[0, 1], [-1, 6]], n % O)

m = [[1, 0], [0, 1]]
s = 0
for v in input().split():
    x = int(v) % O
    s += x
    q = A(2 * x)
    q[0][0] += 1
    q[1][1] += 1
    m = ml(m, q)

m = ml(m, A(-s))
print((m[0][0] + m[0][1] * 3) % M)
