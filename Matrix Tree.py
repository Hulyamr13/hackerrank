# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 1000000007


def go(u, k, adj, vis, val):
    ret = val[u] - k + MOD
    if ret >= MOD:
        ret -= MOD
    vis[u] = True
    for i in range(len(adj[u]) - 1, -1, -1):
        v = adj[u][i]
        if not vis[v]:
            ret *= go(v, val[u], adj, vis, val)
            ret %= MOD
    return ret


if __name__ == "__main__":
    n = int(input())
    val = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    vis = [False] * (n + 1)

    values = list(map(int, input().split()))
    for i in range(1, n + 1):
        val[i] = values[i - 1]

    for i in range(1, n):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    result = go(1, 0, adj, vis, val)
    print(result)
