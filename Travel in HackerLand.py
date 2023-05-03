#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'travel' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY t
#  2. 2D_INTEGER_ARRAY roads
#  3. 2D_INTEGER_ARRAY queries
#

import heapq

def root(ids, i):
    while ids[i] != i:
        ids[i] = ids[ids[i]]
        i = ids[i]
    return i

def union(queries, blds, ids, p, q):
    i = root(ids, p)
    j = root(ids, q)
    if i == j:
        return i, j
    if len(blds[i]) > len(blds[j]):
        bigb, smb = blds[i], blds[j]
    else:
        bigb, smb = blds[j], blds[i]
    for b in smb:
        bigb.add(b)
    del smb
    if len(queries[i][0]) + len(queries[i][1]) > len(queries[j][0]) + len(queries[j][1]):
        ids[j] = i
        blds[i] = bigb
        blds[j] = None
        return j, i
    else:
        ids[i] = j
        blds[j] = bigb
        blds[i] = None
        return i, j

def travel(t, roads, queries):
    n = len(t)
    edges = []
    for i in range(len(roads)):
        x, y, u = roads[i]
        edges.append((u, x-1, y-1))
    edges.sort()
    queries_list = [[set([]), []] for _ in range(n)]
    res = [-1 for i in range(len(queries))]
    for qi in range(len(queries)):
        x, y, k = queries[qi]
        x, y = sorted([x-1, y-1])
        if x == y and k <= 1:
            res[qi] = 0
        else:
            qr = (k, x, y, qi)
            if x == y:
                heapq.heappush(queries_list[x][1], qr)
            else:
                queries_list[x][0].add(qr)
                queries_list[y][0].add(qr)
    ids = [i for i in range(n)]
    blds = [set([t[i]]) for i in range(n)]
    for u, x, y in edges:
        i, j = union(queries_list, blds, ids, x, y)
        if i == j:
            continue
        tot_blds = len(blds[j])
        for qr in queries_list[i][0]:
            if root(ids, qr[1]) != root(ids, qr[2]):
                queries_list[j][0].add(qr)
            else:
                queries_list[j][0].discard(qr)
                if tot_blds >= qr[0]:
                    res[qr[-1]] = u
                else:
                    heapq.heappush(queries_list[j][1], qr)
        while queries_list[i][1] and queries_list[i][1][0][0] <= tot_blds:
            res[queries_list[i][1][0][-1]] = u
            heapq.heappop(queries_list[i][1])
        for qr in queries_list[i][1]:
            heapq.heappush(queries_list[j][1], qr)
        queries_list[i][0] = None
        queries_list[i][1] = None
        while queries_list[j][1] and queries_list[j][1][0][0] <= tot_blds:
            res[queries_list[j][1][0][-1]] = u
            heapq.heappop(queries_list[j][1])
    return "\n".join(map(str, res))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    t = list(map(int, input().rstrip().split()))

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = travel(t, roads, queries)

    fptr.write(str(result) + '\n')

    fptr.close()