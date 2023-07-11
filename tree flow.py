from collections import defaultdict
import os
import sys
import heapq

def dijkstra(n, graph, u):
    distance = [float("inf")] * (n + 1)
    distance[u] = 0
    visited = [False] * (n + 1)
    visited[u] = True
    queue = [(distance[u], u)]
    while queue:
        d, u = heapq.heappop(queue)
        for v, w in graph[u]:
            if not visited[v] and distance[v] > d + w:
                visited[v] = True
                distance[v] = d + w
                heapq.heappush(queue, (distance[v], v))
    return distance[1:]

def treeFlow(n, tree):
    graph = defaultdict(list)
    for u, v, w in tree:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return min(sum(dijkstra(n, graph, 1)), sum(dijkstra(n, graph, n)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    tree = []

    for _ in range(n - 1):
        tree.append(list(map(int, input().rstrip().split())))

    result = treeFlow(n, tree)

    fptr.write(str(result) + '\n')

    fptr.close()
