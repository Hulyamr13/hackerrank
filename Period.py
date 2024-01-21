def euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    q = a // b
    g, u, v = euclid(b, a - q * b)
    return (g, v, u - q * v)


def mod_inverse(a, m):
    (g, u, v) = euclid(a, m)
    assert (g == 1)
    return u % m


def d_pow(x, p, one, mul):
    ret = one
    while p > 0:
        if p % 2 == 1:
            ret = mul(ret, x)
        p //= 2
        x = mul(x, x)
    return ret


def d_log(x, y, one, mul, inv, limit):
    step = 1
    while step * step < limit:
        step += 1
    d = dict()
    invx = inv(x)
    cur = mul(invx, y)
    for i in range(1, step + 1):
        if cur not in d:
            d[cur] = i
        cur = mul(cur, invx)
    ret = limit + 1
    cur = one
    xstep = d_pow(x, step, one, mul)
    for i in range(step):
        if cur in d:
            ret = min(ret, step * i + d[cur])
        cur = mul(cur, xstep)
    return -1 if ret == limit + 1 else ret


def multiply(p1, p2):
    a1, b1 = p1
    a2, b2 = p2
    return ((a1 * a2 + b1 * b2 * 5) % m, (a1 * b2 + a2 * b1) % m)


def norm(p):
    a, b = p
    return (a * a - b * b * 5) % m


def inverse(p):
    assert (norm(p) == 1)
    a, b = p
    return (a, -b)


tests = int(input())
for test in range(tests):
    a, b, m = map(int, input().split())
    x = (a, b)
    xlen = norm(x)
    if euclid(xlen, m)[0] != 1:
        print(-1)
        continue
    plen = d_log(xlen, 1, 1, lambda a, b: (a * b) % m, lambda a: mod_inverse(a, m), m)
    x = d_pow(x, plen, (1, 0), multiply)
    pdir = d_log(x, (1, 0), (1, 0), multiply, inverse, 10 * m)
    assert (plen != -1)
    print(plen * pdir)
