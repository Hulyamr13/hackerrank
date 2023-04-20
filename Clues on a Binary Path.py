from collections import deque


def cluesOnBinaryPath(n, m, l, roads):
    g = [[] for _ in range(n + 1)]
    for road in roads:
        u, v, c = road
        g[u].append((v, c))
        g[v].append((u, c))

    used = [False] * ((1 << 20) + 100)
    canMake = [[False] * ((1 << 10) + 100) for _ in range(n + 1)]
    f = [[[[False] * ((1 << 10) + 100) for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

    q_start = deque()
    q_ver = deque()
    q_len = deque()
    q_mask = deque()

    for i in range(1, n + 1):
        f[i][i][0][0] = True
        q_start.append(i)
        q_ver.append(i)
        q_len.append(0)
        q_mask.append(0)

    maxMoves = (l + 1) // 2

    while q_start:
        start = q_start.popleft()
        ver = q_ver.popleft()
        len_ = q_len.popleft()
        mask = q_mask.popleft()

        if len_ == maxMoves:
            continue

        for i in range(len(g[ver])):
            to = g[ver][i][0]
            bit = g[ver][i][1]
            newMask = mask

            if bit == 1:
                newMask += (1 << len_)

            if not f[start][to][len_ + 1][newMask]:
                f[start][to][len_ + 1][newMask] = True
                q_start.append(start)
                q_ver.append(to)
                q_len.append(len_ + 1)
                q_mask.append(newMask)

    maxMask = (1 << maxMoves)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for mask in range(maxMask):
                if f[i][j][maxMoves][mask]:
                    canMake[j][mask] = True

    lengthOfFirstPart = l - maxMoves
    maxMask2 = (1 << lengthOfFirstPart)

    for ver in range(1, n + 1):
        for m1 in range(maxMask2):
            if f[1][ver][lengthOfFirstPart][m1]:
                for m2 in range(maxMask):
                    if canMake[ver][m2]:
                        used[(m1 << maxMoves) + m2] = True

    ans = 0
    maxMaskOverall = (1 << l)

    for i in range(maxMaskOverall):
        if used[i]:
            ans += 1

    return ans


if __name__ == '__main__':
    n, m, l = map(int, input().rstrip().split())
    roads = []
    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    result = cluesOnBinaryPath(n, m, l, roads)

    print(result)
