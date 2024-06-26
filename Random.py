def f(a, c):
    return -n * a * c + a + c

def paw(b, e):
    if e == 0:
        return 0
    if e == 1:
        return b
    if e & 1:
        return f(b, paw(b, e - 1))
    return paw(f(b, b), e >> 1)

n, a, b = map(int, input().strip().split())
d = list(map(int, input().strip().split()))
nd = [0] * n

ia = 2 / (n * (n - 1))
x = paw(ia, a)
y = 1 - (n - 1) * x

for i in range(n):
    s = 0
    for j in range(n):
        s += d[j] * (y if i == j else x)
    nd[i] = s

if b:
    mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                k = min(i + 1, n - i) - 1 + i * (i - 1) // 2 + (n - i - 1) * (n - i - 2) // 2
            else:
                k = min(min(i, j) + 1, n - max(i, j))
            mat[i][j] = (k * 2) / (n * (n - 1))

    for _ in range(b):
        for i in range(n):
            d[i] = 0
            for j in range(n):
                d[i] += mat[i][j] * nd[j]
        for i in range(n):
            nd[i] = d[i]

s = 0
for i in range(n):
    k = (i + 1) * (n - i) - 1
    s += nd[i] * k

print("%.11f" % ((s * 2) / (n * (n - 1))))
