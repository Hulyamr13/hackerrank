maxn = 155
area = [[False] * maxn for _ in range(maxn)]
hnum = [[0] * maxn for _ in range(maxn)]
vnum = [[0] * maxn for _ in range(maxn)]
vdeg = [0] * (maxn * maxn)
hdeg = [0] * (maxn * maxn)
first = [-1] * maxn
next_ = [-1] * (maxn * maxn * 4)
to = [-1] * (maxn * maxn * 4)
from_ = [-1] * (maxn * maxn * 4)
cap = [-1] * (maxn * maxn * 4)
cost = [-1] * (maxn * maxn * 4)
ecnt = 0

def add_edge(u, v, _cap, _cost):
    global ecnt
    next_[ecnt] = first[u]
    to[ecnt] = v
    from_[ecnt] = u
    cap[ecnt] = _cap
    cost[ecnt] = _cost
    first[u] = ecnt
    ecnt += 1
    next_[ecnt] = first[v]
    to[ecnt] = u
    from_[ecnt] = v
    cap[ecnt] = 0
    cost[ecnt] = -_cost
    first[v] = ecnt
    ecnt += 1

inq = [False] * maxn
q = [-1] * maxn
dist = [0] * maxn
h = [0] * maxn

def push_flow(S, T):
    for i in range(T + 1):
        inq[i] = False
        dist[i] = int(1e9)
        h[i] = -1

    ql = 0
    qr = 0
    dist[S] = 0
    h[S] = -1
    q[qr] = S
    qr += 1
    inq[S] = True

    while ql != qr:
        cur = q[ql]
        inq[cur] = False
        ql += 1
        if ql == maxn:
            ql = 0

        i = first[cur]
        while i != -1:
            if cap[i] > 0 and dist[to[i]] > dist[cur] + cost[i]:
                dist[to[i]] = dist[cur] + cost[i]
                h[to[i]] = i
                if not inq[to[i]]:
                    q[qr] = to[i]
                    inq[to[i]] = True
                    qr += 1
                    if qr == maxn:
                        qr = 0
            i = next_[i]

    if dist[T] == int(1e9):
        return -1

    cur = T
    pcost = 0
    while h[cur] != -1:
        cap[h[cur]] -= 1
        cap[h[cur] ^ 1] += 1
        pcost += cost[h[cur]]
        cur = from_[h[cur]]

    return pcost

def main():
    n, k = map(int, input().split())
    for i in range(n):
        row = input().strip()
        for j in range(n):
            if row[j] == '#':
                area[i][j] = False
            else:
                area[i][j] = True

    hcnt = 0
    vcnt = 0
    for i in range(n):
        for j in range(n):
            if area[i][j]:
                if j == 0 or not area[i][j - 1]:
                    hnum[i][j] = hcnt
                    hcnt += 1
                else:
                    hnum[i][j] = hnum[i][j - 1]

    for j in range(n):
        for i in range(n):
            if area[i][j]:
                if i == 0 or not area[i - 1][j]:
                    vnum[i][j] = vcnt
                    vcnt += 1
                else:
                    vnum[i][j] = vnum[i - 1][j]

    S = hcnt + vcnt
    T = hcnt + vcnt + 1
    for i in range(hcnt):
        for j in range(hdeg[i]):
            add_edge(S, i, 1, j)

    for i in range(vcnt):
        for j in range(vdeg[i]):
            add_edge(i + hcnt, T, 1, j)

    for i in range(n):
        for j in range(n):
            if area[i][j]:
                add_edge(hnum[i][j], vnum[i][j] + hcnt, 1, 0)

    res = 0
    for _ in range(k):
        z = push_flow(S, T)
        res += z

    print(res)

if __name__ == "__main__":
    main()