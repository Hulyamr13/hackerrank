import array as arr
from typing import List

K = 150

n, m = map(int, input().split())

edgesList = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    edgesList[u-1].append(v-1)
    edgesList[v-1].append(u-1)

edges = [[] for i in range(n)]
for i in range(n):
    edges[i] = sorted(edgesList[i])

ar = arr.array('l', [0]*(m*K))
arLen = 0
ans = 0
col = [False]*n

for i in range(n):
    if len(edges[i]) <= K:
        for it in range(len(edges[i])):
            for jt in range(it+1, len(edges[i])):
                ar[arLen] = n*edges[i][it] + edges[i][jt]
                arLen += 1
    else:
        col = [False]*n
        for j in edges[i]:
            col[j] = True
        for j in range(n):
            if len(edges[j]) > K and j <= i:
                continue
            cnt = 0
            for k in edges[j]:
                if col[k]:
                    cnt += 1
            ans += cnt*(cnt-1)//2

ar = sorted(ar[0:arLen])

i = 0
while i < arLen:
    j = i
    while j < arLen and ar[i] == ar[j]:
        j += 1
    cnt = j - i
    ans += cnt*(cnt-1)//2
    i = j

if ans % 2 != 0:
    raise AssertionError()

print(ans//2)
