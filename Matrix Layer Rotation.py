M, N, R = map(int, input().split())
mx = []

for i in range(M):
    mx.append(list(map(int, input().split())))

my = []
for k in range(min(M, N) // 2):
    tmp = []
    i = j = k
    m, n = M - k, N - k
    while i < m - 1:
        tmp.append(mx[i][j])
        i += 1
    while j < n - 1:
        tmp.append(mx[i][j])
        j += 1
    while i > k:
        tmp.append(mx[i][j])
        i -= 1
    while j > k:
        tmp.append(mx[i][j])
        j -= 1
    my.append(tmp[-(R % len(tmp)):] + tmp[:-(R % len(tmp))])

for k in range(len(my)):
    tmp = []
    c = 0
    i = j = k
    m, n = M - k, N - k
    while i < m - 1:
        mx[i][j] = my[k][c]
        i += 1
        c += 1
    while j < n - 1:
        mx[i][j] = my[k][c]
        j += 1
        c += 1
    while i > k:
        mx[i][j] = my[k][c]
        i -= 1
        c += 1
    while j > k:
        mx[i][j] = my[k][c]
        j -= 1
        c += 1

for a in mx:
    print(' '.join(map(str, a)))