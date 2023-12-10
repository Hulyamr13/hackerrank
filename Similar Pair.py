import resource
import sys

sys.setrecursionlimit(2000000)


def add(x, v):
    x += 1
    while x <= n:
        a[x] += v
        x += x & -x


def que(x):
    x += 1
    if x <= 0:
        return 0
    ret = 0
    x = min(n, x)
    while x > 0:
        ret += a[x]
        x -= x & -x
    return ret


st = []
vis = {}


def dfs(x):
    global ans
    st.append(x)
    while st:
        x = st[-1]
        if not x in vis:
            ans += que(x + T) - que(x - T - 1)
            add(x, 1)
            vis[x] = 1
        if nx[x]:
            st.append(nx[x][-1])
            nx[x].pop()
        else:
            st.pop()
            add(x, -1)


n, T = (int(x) for x in input().split())
a = [0 for i in range(4 * n)]
nx = [[] for i in range(n)]
pre = [-1 for i in range(n)]
for i in range(n - 1):
    s, e = (int(x) - 1 for x in input().split())
    nx[s].append(e)
    pre[e] = s

s = 1
while pre[s] != -1:
    s = pre[s]
ans = 0
dfs(s)
print(ans)