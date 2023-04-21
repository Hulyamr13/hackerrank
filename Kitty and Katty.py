import math

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a = a % b
        a, b = b, a
    return a

def ext_gcd(A, B):
    x2, y2 = 1, 0
    x1, y1 = 0, 1
    r2, r1 = A, B
    while r1 != 0:
        q = r2 // r1
        r = r2 % r1
        x = x2 - (q * x1)
        y = y2 - (q * y1)
        r2, r1 = r1, r
        x2, y2 = x1, y1
        x1, y1 = x, y
    return x2, y2, r2

def mod_inv(a, m):
    x, y, _ = ext_gcd(a, m)
    if x < 0:
        x += m
    return x

def power(a, p):
    res = 1
    x = a
    while p:
        if p & 1:
            res = res * x
        x = x * x
        p >>= 1
    return res

def big_mod(a, p, m):
    res = 1 % m
    x = a % m
    while p:
        if p & 1:
            res = res * x % m
        x = x * x % m
        p >>= 1
    return res

def solution():
    kase = int(input())
    for _ in range(kase):
        n = int(input())
        if n == 1:
            print("Kitty")
            continue
        if n & 1:
            print("Katty")
        else:
            print("Kitty")

solution()
