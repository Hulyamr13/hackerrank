P = 1000000007

def pw(x, y):
    s = 1
    t = x
    while y:
        if y & 1:
            s = (s * t) % P
        t = (t * t) % P
        y //= 2
    return s

def inv(x):
    return pw(x, P - 2)

F = [0] * 1010
IF = [0] * 1010
C = [[0] * 1010 for _ in range(1010)]
D = [[0] * 1010 for _ in range(1010)]

F[0] = 1
for i in range(1, 1010):
    F[i] = (F[i - 1] * i) % P

IF[1010 - 1] = inv(F[1010 - 1])
for i in range(1010 - 2, -1, -1):
    IF[i] = (IF[i + 1] * (i + 1)) % P

for i in range(1010):
    C[i][0] = 1
    for j in range(1, i + 1):
        C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % P

for i in range(1009):
    for j in range(i + 1):
        S = C[i][j]
        if j & 1:
            S = (P - S) % P
        D[i][j + 1] = (D[i][j] + S) % P

_ = int(input())
while _ > 0:
    n, m = map(int, input().split())
    a = [0] * (n + 2)
    for x in map(int, input().split()):
        a[x] += 1
    a[n] += 1
    m += 1
    S = IF[n]
    for i in range(2, n + 1):
        if a[i]:
            S = (S * pw((C[n][i] * F[i - 1]) % P, a[i])) % P
    T = 0
    for i in range(n):
        U = inv(pw(C[n - 1][i], m - 2))
        for j in range(2, n + 1):
            if a[j]:
                W = 0
                le = max(1, i - j + 2)
                ri = min(n - j + 1, i + 1)
                if le <= ri:
                    W = (D[n - j][ri] - D[n - j][le - 1] + P) % P
                    if i & 1:
                        W = (P - W) % P
                U = (U * pw(W, a[j])) % P
        T = (T + U) % P
    S = (S * T) % P
    print(S)
    _ -= 1
