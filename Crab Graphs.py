from math import inf
import queue
def bfs(G, parent, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    q = queue.Queue(maxsize=0)
    q.put(s)
    visited[s] = True
    while not q.empty():
        curr = q.get()
        for v, val in enumerate(G[curr]):
            if not visited[v] and val > 0:
                q.put(v)
                visited[v] = True
                parent[v] = curr
    return visited[t]


def maxFlow(G, s, t):
    n = len(G)
    parent = [None for _ in range(n)]
    max_flow = 0
    while bfs(G, parent, s, t):
        path_flow = inf
        v = t
        while v != s:
            path_flow = min(path_flow, G[parent[v]][v])
            v = parent[v]
        max_flow += path_flow
        v = t
        while v != s:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = parent[v]
    return max_flow


def crabGraphs(n, T, graph):
    G = [[0 for _ in range(2*n + 2)] for _ in range(2*n+2)]
    for u, v in graph:
        G[u-1][n+v-1] = 1
        G[v-1][n+u-1] = 1
    s = 2*n
    t = 2*n + 1
    for u in range(n):
        G[s][u] = min(T, sum(G[u]))
        G[n+u][t] = 1
    return maxFlow(G, s, t)

if __name__ == '__main__':
    c = int(input().strip())

    for c_itr in range(c):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        t = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        graph = []

        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))

        result = crabGraphs(n, t, graph)
        print(result)