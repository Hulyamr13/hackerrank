#!/bin/python3

import math
import os
import random
import re
import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
arr = list(map(int, input().split()))

left_gcd = [0] * (n + 1)
right_gcd = [0] * (n + 2)

for i in range(1, n + 1):
    left_gcd[i] = gcd(left_gcd[i - 1], arr[i - 1])

if n == 1:
    print(arr[0] + 1)
    exit()

for i in range(n, 0, -1):
    right_gcd[i] = gcd(right_gcd[i + 1], arr[i - 1])
    temp = gcd(left_gcd[i - 1], right_gcd[i + 1])
    if arr[i - 1] % temp != 0:
        print(temp)
        exit()


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

