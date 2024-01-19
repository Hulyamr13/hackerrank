from fractions import Fraction as frac
from functools import lru_cache, reduce

@lru_cache(maxsize=None)
def fac(n):
    return 1 if n < 2 else n * fac(n-1)

def bf(k, n):
    s, p, q = [0] * (n-1), 0, fac(n)
    for a in itertools.permutations(range(n)):
        x = sum((1 for i in range(1, n-1) if (a[i]-a[i-1])*(a[i]-a[i+1]) > 0))
        s[x] += 1
        p += x**k
    return frac(p, q)

@lru_cache(maxsize=None)
def T(n, k):
    if k == 1:
        return 2
    if n < 2 or k < 1 or k >= n:
        return 0
    return T(n-1, k) * k + 2 * T(n-1, k-1) + (n-k) * T(n-1, k-2)

def S(n, k):
    return T(n, k+1)

@lru_cache(maxsize=None)
def f(n, k):
    return frac(sum(j**k * S(n, j) for j in range(n-1)), fac(n))

def sample(k):
    for i in range(k+1):
        yield (i+15, f(i+15, k))

def F(n, k):
    if n < 15:
        return f(n, k)
    ret = frac(0)
    for t in sample(k):
        if n == t[0]:
            return t[1]
        ret += t[1] * reduce(lambda x, y: x*y, [frac(n-s[0], t[0]-s[0]) for s in sample(k) if s[0] != t[0]])
    return ret

k, n = map(int, input().split())
ans = F(n, k)
print(f"{ans.numerator} / {ans.denominator}")
