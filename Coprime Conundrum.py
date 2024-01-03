#!/bin/python3

from math import isqrt

def count(v, st, ed):
    return ed // v - st // v

def cal(v, ed):
    ret = 0
    for x in fac[v]:
        ret += mu[x] * count(x, v, ed)
    return ret

MAXN = 112345

mu = [0] * MAXN
fac = [[] for _ in range(MAXN)]

mu[1] = 1
for i in range(1, MAXN):
    for j in range(i * 2, MAXN, i):
        mu[j] -= mu[i]

for i in range(1, MAXN):
    if mu[i]:
        for j in range(i, MAXN, i):
            fac[j].append(i)

n = int(input())
ans = 0
for i in range(2, isqrt(n) + 1):
    ans += cal(i, n // i)

print(ans)
