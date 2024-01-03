mod = 10**9 + 7

def f(*rs):
    v = 1
    for a, b in rs:
        v *= max(0, b - a + 1)
        v %= mod
        if not v:
            break
    return v

def comb2(pair1, pair2):
    a, b = pair1
    c, d = pair2
    return max(a, c), min(b, d)

def comb(*rs):
    result = rs[0]
    for pair in rs[1:]:
        result = comb2(result, pair)
    return result

def f211(a, b, c, d):
    return f(comb(a, b), c, d)

def f31(a, b, c, d):
    return f(comb(a, b, c), d)

def f22(a, b, c, d):
    return f(comb(a, b), comb(c, d))

def f4(a, b, c, d):
    return f(comb(a, b, c, d))

z = int(input())
for cas in range(z):
    l1, r1, l2, r2, l3, r3, l4, r4 = map(int, input().strip().split())

    s = f((l1, r1), (l2, r2), (l3, r3), (l4, r4))
    s -= f211((l1, r1), (l2, r2), (l3, r3), (l4, r4))
    s -= f211((l2, r2), (l3, r3), (l4, r4), (l1, r1))
    s -= f211((l3, r3), (l4, r4), (l1, r1), (l2, r2))
    s -= f211((l4, r4), (l1, r1), (l2, r2), (l3, r3))
    s += f31((l1, r1), (l2, r2), (l3, r3), (l4, r4))
    s += f31((l2, r2), (l3, r3), (l4, r4), (l1, r1))
    s += f31((l3, r3), (l4, r4), (l1, r1), (l2, r2))
    s += f31((l4, r4), (l1, r1), (l2, r2), (l3, r3))
    s += f22((l1, r1), (l2, r2), (l3, r3), (l4, r4))
    s += f22((l2, r2), (l3, r3), (l4, r4), (l1, r1))
    s -= 3 * f4((l1, r1), (l2, r2), (l3, r3), (l4, r4))
    s %= mod

    print(s)
