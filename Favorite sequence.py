import math
import os
import random
import re
import sys
from collections import defaultdict, deque
import bisect


class Graph:
    def __init__(self, vertices, graph=defaultdict(list), in_coming=defaultdict(int)):
        self.V = vertices  # No. of vertices
        self.graph = graph  # dictionary containing adjacency List
        self.in_coming = in_coming
        self.n = len(vertices)
        # print(self.V)
        # print(self.graph)

    def recursion(self, node, visited, res):
        visited[node] = True
        for c in self.graph[node]:
            if not visited[c]:
                self.recursion(c, visited, res)
        res.append(node)

    def topological_sort(self):
        res = []
        # temp_mark = [False] * self.n
        visited = {node: False for node in self.V}
        for node in self.V:
            if not visited[node]:
                self.recursion(node, visited, res)
                # visited[i] = True
        # res.append(self.V[i])
        return res[::-1]

    def kahn_algo(self):
        res = []
        s = deque([node for node in self.V if node not in self.in_coming])
        while len(s):
            node = s.popleft()
            res.append(node)
            c_list = self.graph[node]
            while len(c_list):
                c = c_list.pop()
                self.in_coming[c] -= 1
                if self.in_coming[c] == 0:
                    bisect.insort(s, c)
        return res


def favourite_sequence(n, copies):
    # Write your code here
    edges = defaultdict(list)
    in_coming = defaultdict(int)
    nodes = set()
    # in_coming = set()
    for c_list in copies:
        k = len(c_list)
        # in_coming = in_coming.union(set(c_list[1:]))
        nodes = nodes.union(set(c_list))
        for i in range(k - 1):
            edges[c_list[i]].append(c_list[i + 1])
            in_coming[c_list[i + 1]] += 1

    # no_coming = nodes.difference(in_coming)
    # no_coming = sorted(list(no_coming))
    nodes = sorted(list(nodes))  # reverse=True
    for node in edges.keys():
        edges[node].sort(reverse=True)  # reverse=True

    g = Graph(nodes, edges, in_coming)
    # res = g.topological_sort()
    res = g.kahn_algo()
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    copies = []

    for t_itr in range(n):
        k = int(input())

        copies.append(list(map(int, input().rstrip().split())))

    result = favourite_sequence(n, copies)

    fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    fptr.close()