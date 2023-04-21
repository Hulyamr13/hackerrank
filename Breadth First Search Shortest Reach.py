#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

from collections import deque


def bfs(n, m, edges, s):
    # Create an adjacency list to represent the graph
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge
        adj_list[u - 1].append(v - 1)
        adj_list[v - 1].append(u - 1)

    # Initialize the distance array with -1 for unreachable nodes
    distances = [-1] * n
    distances[s - 1] = 0  # Distance to the starting node is 0

    # Perform BFS starting from the given starting node
    queue = deque([s - 1])
    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if distances[v] == -1:
                distances[v] = distances[u] + 6
                queue.append(v)

    # Remove the distance to the starting node from the distance array
    distances.pop(s - 1)

    return distances


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
