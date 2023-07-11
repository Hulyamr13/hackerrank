import sys


def augment(x):
    if vis[x]:
        return False
    vis[x] = True
    for i in range(len(adj[x])):
        if inv[adj[x][i]] == -1 or augment(inv[adj[x][i]]):
            match[x] = adj[x][i]
            inv[adj[x][i]] = x
            return True
    return False


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    v = list(map(int, input().split()))
    adj = [[] for _ in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            if abs(v[i] - v[j]) >= K:
                adj[i].append(j)

    match = [-1] * N
    inv = [-1] * N
    ans = 0

    for i in range(N):
        if match[i] == -1:
            vis = [False] * N
            augment(i)

    for i in range(N):
        if inv[i] == -1:
            ans += 1

    print(ans)
