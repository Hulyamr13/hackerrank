import sys

sys.setrecursionlimit(10**7)

N = 1031

def dfs(a, b):
    used[a][b] = 1
    for i in range(len(g[a])):
        to = g[a][i][0]
        cost = g[a][i][1]
        cost |= b
        if used[to][cost]:
            continue
        dfs(to, cost)

n, m = map(int, input().split())

g = [[] for _ in range(N)]
used = [[0] * N for _ in range(N)]

for i in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

a, b = map(int, input().split())
dfs(a, 0)

ans = 0
while ans < 1024 and used[b][ans] == 0:
    ans += 1
if ans == 1024:
    ans = -1
print(ans)
