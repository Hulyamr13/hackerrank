#!/bin/python3

import sys
from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def smallest_multiple(n):
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        result = smallest_multiple(n)
        print(result)