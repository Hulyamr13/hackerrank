#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

import heapq


def prims(n, edges, start):
    # Create an adjacency list to represent the graph
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        u, v, weight = edge
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    # Initialize the MST with the starting node
    mst = set([start])
    # Use a priority queue to store edges with the minimum weight
    pq = [(weight, start, v) for v, weight in graph[start]]
    heapq.heapify(pq)
    total_weight = 0

    while pq:
        weight, u, v = heapq.heappop(pq)
        # If the edge connects a node not in the MST to a node in the MST,
        # add it to the MST and update the total weight
        if v not in mst:
            mst.add(v)
            total_weight += weight
            for w, weight_w in graph[v]:
                if w not in mst:
                    heapq.heappush(pq, (weight_w, v, w))

    return total_weight


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()