MOD = 1000000007

def ipow(b, e):
    if e == 1:
        return b
    if e & 1:
        return ipow(b, e - 1) * b % MOD
    return ipow(b * b % MOD, e >> 1)

def mmul(c, d, g, h):
    dh = d * h
    rx = ((c + d) * (g + h) - dh) % MOD
    ry = (c * g + dh) % MOD
    return rx, ry

def mpow(e):
    if e == 1:
        return 1, 0
    elif e & 1:
        rx, ry = mpow(e - 1)
        return mmul(1, 0, rx, ry)
    else:
        rx, ry = mpow(e >> 1)
        return mmul(rx, ry, rx, ry)

L = 10000000
F = [0] * L
F[1] = 1

def Fm(n):
    if n < L:
        return F[n]

    rx, ry = mpow(n)
    return rx

dset = set()
a = set()

n = int(input())
for _ in range(n):
    v = int(input())
    a.add(v)

for x in a:
    if x <= 2:
        continue
    for d in range(1, int(x**0.5) + 1):
        if x % d == 0:
            dset.add(d)
            dset.add(x // d)

ds = sorted(list(dset))

cs = [1] * len(ds)
ans = 1

for i in range(len(ds) - 1, -1, -1):
    for j in range(len(ds) - 1, i, -1):
        if ds[j] % ds[i] == 0:
            cs[i] -= cs[j]

    c = cs[i] % (MOD - 1)
    if c < 0:
        c += MOD - 1
    if c:
        f = Fm(ds[i])
        if f != 1:
            ans *= ipow(f, c)
            ans %= MOD

if ans < 0:
    ans += MOD

print(ans)
