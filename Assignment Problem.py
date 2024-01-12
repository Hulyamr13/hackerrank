import sys
read = lambda t=int: list(map(t,sys.stdin.readline().split()))
array = lambda *ds: [array(*ds[1:]) for _ in range(ds[0])] if ds else 0

# Method one: turns out too slow due to big integers
from operator import mul
from functools import reduce, lru_cache
@lru_cache(maxsize=10**5)
def binom(n, k):
    if n-k < k: k = n-k
    if k < 0: return 0
    return reduce(mul, range(n-k+1,n+1), 1) // reduce(mul, range(1,k+1), 1)
@lru_cache(maxsize=10**5)
def f(x, M, N):
    return sum(binom(N,k)*(-1)**k*binom(N+M-k*x-1,M-k*x) for k in range(M+1))
def solve(M, N):
    r = sum(x*(f(x+1,M,N)-f(x,M,N)) for x in range(M+1))
    r /= f(M+1,M,N)
    return r

# Method two: needs extended precision during the incl/exl
from decimal import Decimal
def f2(x, M, N):
    if x == 0: return 0
    s = Decimal(1)
    q = Decimal(1)
    for k in range(min(M//x,N)):
        q *= Decimal(-(N-k))/Decimal(k+1)
        for j in range(x):
            q *= Decimal((M-k*x-j))/Decimal((N+M-k*x-1-j))
        s += q
    return float(s)
def solve2(M, N):
    bot = 0
    r = 0
    for x in range(1, M+1):
        top = f2(x+1,M,N)
        r += x*(top-bot)
        bot = top
    return r

T, = read()
for _ in range(T):
    M, N = read()
    print(solve2(M,N))