#!/bin/python3

# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#  3. LONG_INTEGER k
#

MOD = 10**9 + 7

comb = [[0] * 110 for _ in range(110)]
dp = [[[0] * 120 for _ in range(120)] for _ in range(110)]

def calc(length, k):
    if length == 0:
        return int(k == 1)

    c5 = 0
    c7 = 0
    c2 = 0
    c3 = 0

    while k % 5 == 0:
        c5 += 1
        k //= 5
        length -= 1

    while k % 7 == 0:
        c7 += 1
        k //= 7
        length -= 1

    while k % 2 == 0:
        c2 += 1
        k //= 2

    while k % 3 == 0:
        c3 += 1
        k //= 3

    if length < 0 or k != 1:
        return 0

    res = dp[length][c2][c3]
    length += c5 + c7
    res = (res * comb[length][c5] * comb[length - c5][c7]) % MOD
    return res

def add(x, y):
    x += y
    if x >= MOD:
        x -= MOD
    return x

def acc(s, k):
    length = len(s)
    res = 0
    cur = 1

    for i in range(1, length):
        res = add(res, calc(i, k))

    for i in range(length):
        x = int(s[i])

        for j in range(1, x):
            nc = cur * j
            if k % nc == 0:
                res = add(res, calc(length - i - 1, k // nc))

        cur *= x
        if x == 0 or k % cur != 0:
            break

    return res

def same(s, k):
    t = 1

    for i in range(len(s)):
        x = int(s[i])
        if t * x > k:
            return False
        t *= x

    return t == k

TC = int(input())
comb[0][0] = 1

for i in range(1, 110):
    comb[i][0] = comb[i][i] = 1
    for j in range(1, i):
        comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

dp[0][0][0] = 1

for i in range(105):
    for j in range(110):
        for k in range(110):
            dp[i + 1][j][k] = add(dp[i + 1][j][k], dp[i][j][k])
            dp[i + 1][j + 1][k] = add(dp[i + 1][j + 1][k], dp[i][j][k])
            dp[i + 1][j][k + 1] = add(dp[i + 1][j][k + 1], dp[i][j][k])
            dp[i + 1][j + 2][k] = add(dp[i + 1][j + 2][k], dp[i][j][k])
            dp[i + 1][j + 1][k + 1] = add(dp[i + 1][j + 1][k + 1], dp[i][j][k])
            dp[i + 1][j + 3][k] = add(dp[i + 1][j + 3][k], dp[i][j][k])
            dp[i + 1][j][k + 2] = add(dp[i + 1][j][k + 2], dp[i][j][k])

for tc in range(TC):
    print("Case {}: ".format(tc + 1), end="")
    a, b, k = input().split()
    k = int(k)
    result = acc(b, k) - acc(a, k) + same(b, k)
    result = (result + MOD) % MOD
    print(result)

