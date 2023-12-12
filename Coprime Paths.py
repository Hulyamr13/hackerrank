from collections import defaultdict

N = 25123
LN = 15
MaxVal = 10000000

adj = defaultdict(list)
depth = [0] * N
parent = [[-1] * N for _ in range(LN)]
ST = [0] * N
EN = [0] * N
cur_time = 0
vec = [0] * (2 * N)
primes = [[] for _ in range(N)]
upd = [[] for _ in range(N)]
pr = [0] * (MaxVal + 1)
S = 0
ans = [0] * N
used = [False] * N
vp = [[0] * (4 * N) for _ in range(3)]

def dfs(u=0, d=0, prev=-1):
    global cur_time
    depth[u] = d
    parent[0][u] = prev
    ST[u] = cur_time
    vec[ST[u]] = u
    cur_time += 1

    for v in adj[u]:
        if v == prev:
            continue
        dfs(v, d + 1, u)

    EN[u] = cur_time
    vec[EN[u]] = u
    cur_time += 1

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    diff = depth[u] - depth[v]
    for i in range(LN):
        if (diff >> i) & 1:
            u = parent[i][u]

    if u == v:
        return u

    for i in range(LN - 1, -1, -1):
        if parent[i][u] != parent[i][v]:
            u = parent[i][u]
            v = parent[i][v]

    return parent[0][u]

if __name__ == '__main__':
    for i in range(2, MaxVal + 1):
        if not pr[i]:
            for j in range(i + i, MaxVal + 1, i):
                if not pr[j]:
                    pr[j] = i

    n, q = map(int, input().split())
    S = int((2 * n) ** 0.5)

    p1 = {}
    p2 = {}
    p3 = {}

    for i in range(n):
        x = int(input())
        v = primes[i]
        while pr[x]:
            v.append(pr[x])
            x //= pr[x]
        if x > 1:
            v.append(x)
        v = list(set(v))
        v.sort()

        for k in range(len(v)):
            if v[k] in p1:
                id = p1[v[k]]
            else:
                p1[v[k]] = len(p1)
                id = p1[v[k]]
            upd[i].append((0, id))

            for j in range(k + 1, len(v)):
                tmp = (v[k], v[j])
                if tmp in p2:
                    id = p2[tmp]
                else:
                    p2[tmp] = len(p2)
                    id = p2[tmp]
                upd[i].append((1, id))

        if len(v) == 3:
            tmp = (v[0], v[1], v[2])
            if tmp in p3:
                id = p3[tmp]
            else:
                p3[tmp] = len(p3)
                id = p3[tmp]
            upd[i].append((2, id))

    for i in range(1, n):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    dfs()

    for i in range(1, LN):
        for j in range(n):
            if parent[i - 1][j] != -1:
                parent[i][j] = parent[i - 1][parent[i - 1][j]]

    queries = []
    for _ in range(q):
        u, v = map(int, input().split())
        u -= 1
        v -= 1

        if ST[u] > ST[v]:
            u, v = v, u

        p = lca(u, v)
        if p == u:
            queries.append((ST[u], ST[v], len(queries), -1))
        else:
            queries.append((EN[u], ST[v], len(queries), p))

    queries.sort(key=lambda x: (x[0] // S, -x[1]))

    active = 0
    cur = 0

    def insert(u):
        nonlocal active, cur
        tmp = active

        for p in upd[u]:
            if p[0] & 1:
                tmp += vp[p[0]][p[1]]
            else:
                tmp -= vp[p[0]][p[1]]

        cur += tmp
        used[u] = True
        active += 1

        for p in upd[u]:
            vp[p[0]][p[1]] += 1

    def remove(u):
        nonlocal active, cur
        used[u] = False
        active -= 1

        for p in upd[u]:
            vp[p[0]][p[1]] -= 1

        tmp = active
        for p in upd[u]:
            if p[0] & 1:
                tmp += vp[p[0]][p[1]]
            else:
                tmp -= vp[p[0]][p[1]]

        cur -= tmp

    L = 0
    R = -1
    for t in queries:
        l, r, i, p = t
        while R < r:
            R += 1
            if used[vec[R]]:
                remove(vec[R])
            else:
                insert(vec[R])

        while R > r:
            if used[vec[R]]:
                remove(vec[R])
            else:
                insert(vec[R])
            R -= 1

        while L < l:
            if used[vec[L]]:
                remove(vec[L])
            else:
                insert(vec[L])
            L += 1

        while L > l:
            L -= 1
            if used[vec[L]]:
                remove(vec[L])
            else:
                insert(vec[L])

        ans[i] = cur
        if p != -1:
            tmp = active
            for k in upd[p]:
                if k[0] & 1:
                    tmp += vp[k[0]][k[1]]
                else:
                    tmp -= vp[k[0]][k[1]]
            ans[i] += tmp

    for i in range(q):
        print(ans[i])
