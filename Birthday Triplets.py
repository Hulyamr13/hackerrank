#!/bin/python3

from math import floor, sqrt

MOD = 10 ** 9 + 7

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = floor(sqrt(n))
    return sqrt_n * sqrt_n == n

def find_abc(f2, f3, f4):
    a = -1
    b = -1
    c = -1
    for _a in range(1, 15001):
        x = f2 - _a ** 2
        y = f3 - _a ** 3
        z = f4 - _a ** 4
        d = 2 * z - x ** 2
        if is_perfect_square(d):
            c = int(x - sqrt(d))
            if not (c & 1):
                c //= 2
                b = x - c
                if is_perfect_square(b):
                    b = int(sqrt(b))
                    c = int(sqrt(c))
                    if _a < b and b ** 3 + c ** 3 == y:
                        a = _a
        if a != -1:
            break
    return a, b, c

def geometric_progression_sum(a, l, r):
    if a == 1:
        return r - l + 1
    return ((pow(a, r + 1, MOD) - pow(a, l, MOD) + MOD) % MOD * pow(a - 1, MOD - 2, MOD)) % MOD

if __name__ == '__main__':
    for _ in range(int(input())):
        f2, f3, f4, l, r = map(int, input().split())
        a, b, c = find_abc(f2, f3, f4)
        print((geometric_progression_sum(a, l, r) + geometric_progression_sum(b, l, r) + geometric_progression_sum(c, l, r)) % MOD)
