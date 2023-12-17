#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hanoi' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY posts as parameter.
#

from collections import deque


def tuplify(x):
    return tuple(tuple(i) for i in x)


def moves(rods):
    for x in range(4):
        if rods[x]:
            for y in range(4):
                if not rods[y] or rods[y][-1] > rods[x][-1]:
                    yield (x, y)


def do_move(rods, x, y):
    rods = [list(r) for r in rods]
    rods[y].append(rods[x].pop())
    rods[1:4] = sorted(rods[1:4], key=lambda t: t[-1] if t else 0)
    return tuplify(rods)


def bfs(rods, n):
    start = (tuplify(rods), 0)
    visited = set()
    visited.add(start)
    q = deque([start])
    while q:
        cur, depth = q.popleft()
        if all(len(r) == 0 for r in cur[1:]):
            return depth
        for x, y in moves(cur):
            child = do_move(cur, x, y)
            if child not in visited:
                visited.add(child)
                q.append((child, depth + 1))
    return -1


def hanoi(posts):
    rods = [[] for _ in range(4)]
    for i, disk in enumerate(posts):
        rods[disk - 1] = [i] + rods[disk - 1]
    return bfs(rods, len(posts))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    loc = list(map(int, input().rstrip().split()))

    res = hanoi(loc)

    fptr.write(str(res) + '\n')

    fptr.close()
