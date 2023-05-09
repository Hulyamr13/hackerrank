#!/bin/python3

import os
import random
import re
import sys
from math import gcd

def longestModPath(corridor, queries):
    n = len(corridor)
    adj = [[] for i in range(n)]
    for i in range(n):
        a, b, c = corridor[i]
        a -= 1; b -= 1
        adj[a].append((b, c))
        adj[b].append((a, -c))

    dist = [None]*n
    parents = [set() for i in range(n)] # set because of special case: cycle of length 2
    dist[0] = 0
    stack = [0]
    while stack:
        i = stack.pop()
        for j, c in adj[i]:
            if j in parents[i]: continue
            ndist = dist[i] + c
            parents[j].add(i)
            if dist[j] is None:
                dist[j] = ndist
                stack.append(j)
            else:
                cycle = abs(dist[j] - ndist)

    res = []
    for i in range(len(queries)):
        s, e, m = queries[i]
        a = gcd(cycle, m)
        res.append(m - a + (dist[e-1] - dist[s-1]) % a)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    corridor = []

    for _ in range(n):
        corridor.append(list(map(int, input().rstrip().split())))

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = longestModPath(corridor, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()