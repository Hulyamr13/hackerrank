#!/bin/python3

import os
import sys

#
# Complete the treePrunning function below.
#

from collections import defaultdict

INF = -(1e15)


def dfs(x, f, g, k, weights):
    dpc = [INF] * (k + 1)
    dpc[0] = weights[x]

    for n in g[x]:
        if n == f:
            continue
        dpn = dfs(n, x, g, k, weights)
        dptmp = [INF] * (k + 1)
        for i in range(k + 1):
            if dpc[i] == INF:
                break
            for j in range(0, k - i + 1):
                if dpn[j] == INF:
                    break
                dptmp[i + j] = max(dptmp[i + j], dpc[i] + dpn[j])
            if i + 1 <= k:
                dptmp[i + 1] = max(dptmp[i + 1], dpc[i])
        dpc = dptmp
    return dpc


def treePrunning(k, weights, edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    dpn = dfs(0, -1, g, k, weights)
    return max(max(dpn), 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    weights = list(map(int, input().rstrip().split()))

    tree = []

    for _ in range(n - 1):
        tree.append(list(map(int, input().rstrip().split())))

    result = treePrunning(k, weights, tree)

    fptr.write(str(result) + '\n')

    fptr.close()