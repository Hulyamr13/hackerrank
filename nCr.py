from math import factorial


MAX = 38
C = [[0 for _ in range(MAX)] for _ in range(MAX)]


for i in range(MAX):
    for j in range(i + 1):
        if j == 0 or j == i:
            C[i][j] = 1
        else:
            C[i][j] = C[i-1][j-1] + C[i-1][j]


def nCr(n, r):
    if n < r:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)


def lucas(n, r, p):
    assert n >= r
    c = 1
    while r != 0:
        c = (c * C[n % p][r % p]) % p
        n //= p
        r //= p
    return c


def egcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def modinv(a, m):
    g, x, _ = egcd(a, m)
    assert g == 1
    return x % m


def crt(a, n):
    p = 1
    for i in n:
        p *= i
    r = 0
    for ai, ni in zip(a, n):
        r += ai * (p // ni) * modinv(p // ni, ni)
    return r % p


def v(n, p):
    s = 0
    while n != 0:
        n //= p
        s += n
    return s


fa = [1] * 28
for i in range(28):
    fa[i] = (fa[i - 1] * (i if i % 3 != 0 else 1)) % 27

def f_mod27(n):
    return (pow(fa[27], n // 27, 27) * fa[n % 27]) % 27

def fact_mod27(n):
    i = 1
    ret = 1
    while i <= n:
        ret = (ret * f_mod27(n // i)) % 27
        i *= 3
    return ret


def nCr_mod27(n, r):
    e = (v(n, 3) - v(r, 3) - v(n - r, 3))
    return (3 ** e * fact_mod27(n) * modinv(fact_mod27(r) * fact_mod27(n - r), 27)) % 27


def solve(n, r):
    a = [nCr_mod27(n, r), lucas(n, r, 11), lucas(n, r, 13), lucas(n, r, 37)]
    p = [27, 11, 13, 37]
    print(crt(a, p))


for _ in range(int(input())):
    n, r = map(int, input().split())
    solve(n, r)
