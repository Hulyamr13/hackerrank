#!/bin/python3

import os
import sys
import math

# Complete the solve function below.
def count_factors(a, x):
    if x == 1:
        return 0
    if a == 0:
        return 0
    if a % x == 0:
        return 1
    for i in range(100):
        g = math.gcd(a, x)
        if g == x:
            return i + 1
        if g == 1:
            return -1
        x //= g
    return -2


def rec(arr, i, j, count):
    if count == 0:
        return True
    if i > j:
        return count <= 1
    if arr[i] == 0:
        return False
    if arr[i] == 1:
        return count <= 1
    n_cnt = 0
    cur = 1
    while cur < count:
        cur *= arr[i]
        n_cnt += 1
    return rec(arr, i + 1, j, n_cnt)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())

    for _ in range(q):
        i, j, x = map(int, input().split())
        if x == 1:
            print("Yes")
            continue
        i -= 1
        j -= 1
        count = count_factors(arr[i], x)
        if count < 0:
            print("No")
        else:
            ok = rec(arr, i + 1, j, count)
            if ok:
                print("Yes")
            else:
                print("No")
