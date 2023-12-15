#!/bin/python3

import os
import sys
import math

sys.setrecursionlimit(10 ** 6)


def roundup(x):
    k = 1 << (x.bit_length() - 1)
    if k < x:
        return 2 * k
    return k


def update(t, i, x, op):
    t[i] = x
    while i > 1:
        i >>= 1
        t[i] = op(t[2 * i], t[2 * i + 1])


def rangequery(t, a, b, op, init):  # assumes op is of abelian monoid
    s = init
    while a < b:
        if a & 1:
            s = op(s, t[a])
            a += 1
        if b & 1:
            s = op(s, t[b - 1])
            b -= 1
        a >>= 1
        b >>= 1
    return s


def rangeify(l, op, init):
    off = roundup(len(l))
    r = [init for _ in range(off)] + l + [init for _ in range(off - len(l))]
    for i in range(off - 1, 0, -1):
        r[i] = op(r[2 * i], r[2 * i + 1])
    return (r, off)


# Complete the solve function below.
def solve(tree, queries):
    N = len(tree) + 1
    neighbors = [[] for _ in range(N)]

    for edge in tree:
        neighbors[edge[0]].append(edge[1])
        neighbors[edge[1]].append(edge[0])

    heights = []
    eulerian = []
    outs = []
    epos = [[-1, -1] for _ in range(N)]
    heightpos = [-1 for _ in range(N)]

    def dfs(node, parent, height):
        eulerian.append(0)
        epos[node][0] = len(eulerian) - 1
        heights.append((height, node))
        heightpos[node] = len(heights) - 1
        for n in neighbors[node]:
            if n != parent:
                dfs(n, node, height + 1)
                heights.append((height, node))
        eulerian.append(0)
        epos[node][1] = len(eulerian) - 1

    dfs(0, -1, 0)
    htree, hoff = rangeify(heights, lambda x, y: min(x, y), (math.inf, math.inf))
    eulerian, off = rangeify(eulerian, lambda x, y: x + y, 0)
    epos = [[x[0] + off, x[1] + off] for x in epos]
    heightpos = [x + hoff for x in heightpos]

    def lca(u, v):
        low, high = heightpos[u], heightpos[v]
        low, high = min(low, high), max(low, high)
        return rangequery(htree,
                          low,
                          high + 1,
                          lambda x, y: min(x, y),
                          (math.inf, math.inf))

    def pathsum(u, v):
        a = lca(u, v)[1]
        ou = rangequery(eulerian, epos[0][0], epos[u][0] + 1, lambda x, y: x + y, 0)
        ov = rangequery(eulerian, epos[0][0], epos[v][0] + 1, lambda x, y: x + y, 0)
        oa = rangequery(eulerian, epos[0][0], epos[a][0] + 1, lambda x, y: x + y, 0)
        return ou + ov - 2 * oa + eulerian[epos[a][0]]

    for query in queries:
        if query[0] == 1:
            u = query[1]
            x = query[2]
            update(eulerian, epos[u][0], x, lambda x, y: x + y)
            update(eulerian, epos[u][1], -x, lambda x, y: x + y)
        else:
            u = query[1]
            v = query[2]
            outs.append(pathsum(u, v))

    print(htree)
    print(heightpos)
    print(epos)
    print(eulerian, off)
    return outs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    tree = []

    for _ in range(n - 1):
        tree.append(list(map(int, input().rstrip().split())))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(tree, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()