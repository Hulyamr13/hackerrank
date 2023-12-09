#!/bin/python3

import math
import os
import random
import re
import sys
import collections

MOD = 1000000000


#
# Complete the 'countPaths' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#

def countPaths(n, edges):
  graph = collections.defaultdict(list)

  for i, j in edges:
    graph[i - 1].append(j - 1)

  start = 0
  end = n - 1

  memo = [0] * n
  cycle_nodes = set()
  path_nodes = set()

  path = []
  seen = [False] * n

  def update_path_nodes(inc):
    for cur in path:
      path_nodes.add(cur)
      memo[cur] += inc
      memo[cur] %= MOD

  def update_cycle_nodes(cycle_start):
    k = len(path) - 1
    while path[k] != cycle_start:
      cycle_nodes.add(path[k])
      k -= 1
    cycle_nodes.add(cycle_start)

  def dfs(node):
    path.append(node)
    seen[node] = True

    if node == n - 1:
      update_path_nodes(1)
    else:
      for next in graph[node]:
        if seen[next]:
          update_cycle_nodes(next)
        else:
          if memo[next] > 0:
            update_path_nodes(memo[next])
          if memo[next] == 0:
            dfs(next)

    if memo[node] == 0:
      memo[node] = -1

    seen[node] = False
    path.pop()

  dfs(start)
  if len(cycle_nodes.intersection(path_nodes)) > 1:
    print('INFINITE PATHS')
  else:
    print(memo[start])


if __name__ == '__main__':
  first_multiple_input = input().rstrip().split()

  nodes = int(first_multiple_input[0])

  m = int(first_multiple_input[1])

  edges = []

  for _ in range(m):
    edges.append(list(map(int, input().rstrip().split())))

  countPaths(nodes, edges)