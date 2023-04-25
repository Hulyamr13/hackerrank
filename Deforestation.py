#!/bin/python3

import os
import sys
from functools import lru_cache


#
# Complete the deforestation function below.
#
def deforestation(n, tree):
    d = dict()
    for x in tree:
        if x[0] in d:
            d[x[0]].add(x[1])
        else:
            d[x[0]] = set()
            d[x[0]].add(x[1])
        if x[1] in d:
            d[x[1]].add(x[0])
        else:
            d[x[1]] = set()
            d[x[1]].add(x[0])
    dp = [-1 for i in range(n + 1)]

    def r(node, prev):
        if dp[node] == -1:
            dp[node] = 1
            c = 0
            tmp = []
            if node in d:
                for x in d[node]:
                    if x != prev:
                        tmp.append(1 + r(x, node))

            for x in tmp:
                c ^= x
            return c
        else:
            return 0

    c = r(1, -1)
    # print(c)
    if c == 0:
        return "Bob"
    return "Alice"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        tree = []

        for _ in range(n - 1):
            tree.append(list(map(int, input().rstrip().split())))

        result = deforestation(n, tree)

        fptr.write(result + '\n')

    fptr.close()