#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def componentsInGraph(gb):
    # Write your code here
    from collections import defaultdict

    graph = defaultdict(set)

    for u, v in gb:
        graph[u].add(v)
        graph[v].add(u)

    visited = set()
    min_component_size = float('inf')
    max_component_size = float('-inf')

    for node in graph:
        if node not in visited:
            component_size = 0
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    component_size += 1
                    stack.extend(graph[current])

            min_component_size = min(min_component_size, component_size)
            max_component_size = max(max_component_size, component_size)

    return [min_component_size, max_component_size]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
