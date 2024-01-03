#!/bin/python3

import math
import os
import random
import re
import sys


def cw(i, j, k, x, y):
    return (x[i] - x[j]) * (y[k] - y[j]) - (x[k] - x[j]) * (y[i] - y[j])


if __name__ == "__main__":
    n, l = map(int, input().split())
    x = list(map(int, input().split()))

    g = x[0]
    for i in range(1, n):
        g = math.gcd(g, x[i])

    ans = 0
    for d in range(1, int(g**0.5) + 1):
        if g % d == 0:
            if d != 1:
                ans = max(ans, l // d * d)
            if g // d != 1:
                ans = max(ans, l // (g // d) * (g // d))

    print(ans)

