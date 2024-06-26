#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts STRING s as parameter.
#

def relabel(s):
    mapping = {}
    ret = ''
    for x in s:
        if x not in mapping:
            mapping[x] = chr(ord('a') + len(mapping))
        ret += mapping[x]
    return ret

def guass(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for k in range(m):
        i_max = 0
        v_max = matrix[0][k]
        for i in range(1, m):
            if matrix[i][k] > v_max:
                v_max = matrix[i][k]
                i_max = i
        matrix[k], matrix[i_max] = matrix[i_max], matrix[k]
        for i in range(k+1, m):
            for j in range(k+1, n):
                matrix[i][j] -= matrix[k][j] * matrix[i][k] / matrix[k][k]
            matrix[i][k] = 0.0

    ret = [0.0] * m
    for x in range(m-1, -1, -1):
        ret[x] = matrix[x][m] / matrix[x][x]
        for i in range(x-1, -1, -1):
            matrix[i][m] -= ret[x] * matrix[i][x]
    return ret

result = {}

def get(s):
    if s == s[::-1]:
        return 0

    s = relabel(s)
    if s in result:
        return result[s]

    nexts = {}
    ids = {}

    def getnext(s):
        if s not in nexts:
            n = len(s)
            t = []
            if s != s[::-1]:
                for i in range(n):
                    for j in range(i):
                        a = list(s)
                        a[i], a[j] = a[j], a[i]
                        t.append(relabel(''.join(a)))
            nexts[s] = t
            for x in t:
                getnext(x)

    getnext(s)
    #print nexts
    for x in nexts:
        result[x] = 0
        ids[x] = len(ids)

    m = len(ids)
    n = m + 1
    matrix = [[0.0] * n for x in range(m)]
    for x in nexts:
        a = ids[x]
        matrix[a][a] = 1.0
        if len(nexts[x]) == 0:
            continue
        matrix[a][m] = 1.0
        k = len(x) * (len(x) - 1) / 2
        for y in nexts[x]:
            b = ids[y]
            matrix[a][b] -= 1.0/k
    val = guass(matrix)

    for x in nexts:
        result[x] = val[ids[x]]

    return val[ids[s]]

t = int(input())
for _ in range(t):
    s = input().strip()
    print('%.4f' % get(s))