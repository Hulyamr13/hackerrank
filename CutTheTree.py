#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#
from collections import defaultdict


def cutTheTree(data, edges):
    # Write your code here
    edge_map = defaultdict(set)
    for x, y in edges:
        edge_map[x].add(y)
        edge_map[y].add(x)

    # Hierarchical sort
    visited = set()
    ordering = []
    children = defaultdict(list)
    stack = [1]
    while stack:
        node = stack.pop()
        visited.add(node)
        ordering.append(node)

        children[node] = clist = [
            c for c in edge_map[node]
            if c not in visited]
        stack.extend(clist)

    subtree_costs = {}
    for node in reversed(ordering):
        subtree_costs[node] = data[node - 1] + sum(
            subtree_costs[c] for c in children[node])
    total_cost = sum(data)
    return min(abs(total_cost - 2 * subc)
               for subc in subtree_costs.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
