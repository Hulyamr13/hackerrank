def solve2(n, m, d):
    r = 0
    s = set([])
    for k, v in d.items():
        dc = {}
        for x in v:
            if x not in s and x in d:
                for y in d[x]:
                    if y not in s:
                        if y in dc:
                            dc[y] += 1
                        else:
                            dc[y] = 1
        for node, c in dc.items():
            if node != k:
                r += c * (c - 1) // 2
        s.add(k)
    return r


n, m = map(int, input().strip().split())
d = {}
for i in range(m):
    x, y = map(int, input().strip().split())
    if x in d:
        d[x].append(y)
    else:
        d[x] = [y]
    if y in d:
        d[y].append(x)
    else:
        d[y] = [x]

print(solve2(n, m, d))