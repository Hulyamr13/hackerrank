from random import randint

def inv(a, b):
    return pow(a, b-2, b)

def lagrange(v, k, x, mod):
    if x <= k:
        return v[x]
    inn, den = 1, 1
    for i in range(1, k + 1):
        inn = (inn * (x - i)) % mod
        den = (den * (mod - i)) % mod
    inn = (inn * inv(den, mod)) % mod
    ret = 0
    for i in range(k + 1):
        ret = (ret + v[i] * inn) % mod
        md1 = mod - ((x - i) * (k - i)) % mod
        md2 = ((i + 1) * (x - i - 1)) % mod
        if i != k:
            inn = (((inn * md1) % mod) * inv(md2, mod)) % mod
    return ret

def ilog2(n):
    return 0 if n <= 0 else n.bit_length() - 1

def pack(pack, shamt):
    size = len(pack)
    while size > 1:
        npack = []
        for i in range(0, size - 1, 2):
            npack += [pack[i] | (pack[i+1] << shamt)]
        if size & 1:
            npack += [pack[-1]]
        pack, size, shamt = npack, (size + 1) >> 1, shamt << 1
    return pack[0]

def unpack(M, size, shamt):
    s, sizes = size, []
    while s > 1:
        sizes += [s]
        s = (s + 1) >> 1
    ret = [M]
    for size in sizes[::-1]:
        mask, nret = (1 << shamt) - 1, []
        for c in ret:
            nret += [c & mask, c >> shamt]
        ret, shamt = nret[:size], shamt >> 1
    return ret

def poly_mul_mod(f, g, mod):
    size = min(len(f), len(g))
    shift = ((mod - 1) ** 2 * size).bit_length()
    rsize = len(f) + len(g) - 1
    h = unpack(pack(f, shift) * pack(g, shift), rsize, shift * (1 << ilog2(rsize - 1)))
    return [int(x % mod) for x in h]

def solve(n, k, mod):
    mul = n * pow(2, ((n - 1) * (n - 2)) // 2, mod)
    n -= 1
    fact = [1] * (k + 10)
    for i in range(2, k + 10):
        fact[i] = (i * fact[i - 1]) % mod
    f = []
    g = []
    for i in range(0, k + 5):
        _inv = inv(fact[i], mod)
        f.append(_inv)
        g.append((pow(i, k, mod) * _inv) % mod)
    h = poly_mul_mod(f, g, mod)
    del h[(k + 1):]
    pw = pow(2, k, mod)
    for i in range(0, k + 1):
        h[i] = (h[i] * fact[i]) % mod
        _inv = inv(pow(2, i, mod), mod)
        h[i] = (h[i] * pw * _inv) % mod
    return (mul * pow(2, n, mod) * inv(pw, mod) * lagrange(h, k, n, mod)) % mod

for t in range(int(input())):
    n, k = map(int, input().split())
    print(solve(n, k, 1005060097))