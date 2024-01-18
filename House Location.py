from math import sqrt, fabs

def eq(x, y):
    return fabs(x - y) < 1e-8

def get(x1, y1, x2, y2, a):
    t = a * a - 1  # we are given 1 < a <= 1000, so t cannot be 0.
    z1 = (2 * x1 - 2 * a * a * x2) / t
    z2 = (2 * y1 - 2 * a * a * y2) / t
    z3 = (a * a * (x2 * x2 + y2 * y2) - x1 * x1 - y1 * y1) / t
    x = -z1 / 2
    y = -z2 / 2
    r = x * x + y * y - z3
    return x, y, r

def solve(c1, c2):
    a, b, r = c1
    c, d, s = c2
    e = c - a
    f = d - b
    p2 = e ** 2 + f ** 2
    if eq(p2, 0):
        if eq(r, s):  # same circle
            return a - sqrt(r), b
        else:
            return None
    p = sqrt(p2)
    k = (p2 + r - s) / (2 * p)
    if eq(r, k ** 2):
        r = k ** 2
    elif r < k ** 2:
        return None
    x1 = a + e * k / p + (f / p) * sqrt(r - k ** 2)
    y1 = b + f * k / p - (e / p) * sqrt(r - k ** 2)
    x2 = a + e * k / p - (f / p) * sqrt(r - k ** 2)
    y2 = b + f * k / p + (e / p) * sqrt(r - k ** 2)
    if eq(x1, x2):
        return x1, min(y1, y2)
    elif x1 < x2:
        return x1, y1
    else:
        return x2, y2

def doit():
    a, b = map(float, input().strip().split())
    x1, y1 = map(float, input().strip().split())
    x2, y2 = map(float, input().strip().split())
    x3, y3 = map(float, input().strip().split())
    x4, y4 = map(float, input().strip().split())
    c1 = get(x1, y1, x2, y2, a)
    c2 = get(x3, y3, x4, y4, b)
    if c1 is None or c2 is None:
        return None
    return solve(c1, c2)

root = doit()
if root is None:
    print('Impossible!')
else:
    print('%.2f %.2f' % (root[0] + 1e-5, root[1] + 1e-5))
