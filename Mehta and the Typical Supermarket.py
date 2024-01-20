#!/bin/python3
import os
from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

def count_bits(x):
    return bin(x).count('1')

def solve(a, days):
    result = []
    n = len(a)
    bitcount = [0] * (1 << n)
    lcms = [1] * (1 << n)

    for i in range(n):
        for j in range(1 << i):
            lcms[(1 << i) | j] = lcm(a[i], lcms[j])
            bitcount[(1 << i) | j] = count_bits((1 << i) | j)

    def count(k):
        t = 0
        for s in range(1, 1 << n):
            t -= k // lcms[s] * (-1) ** bitcount[s]
        return t

    for day in days:
        l, r = day
        result.append(count(r) - count(l - 1))

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())
    a = []
    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    d = int(input().strip())
    days = []
    for _ in range(d):
        days.append(list(map(int, input().rstrip().split())))

    result = solve(a, days)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
