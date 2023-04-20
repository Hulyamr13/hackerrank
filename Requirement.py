INF = 9999
MOD = 1007

class list:
    def __init__(self, mask):
        self.mask = mask
        self.next = None

def min(x, y):
    return y if x > y else x

def findleft(mask, n):
    for i in range(n):
        if (1 << i) & mask:
            flag = 0
            for j in range(n):
                if ((1 << j) & mask) and i != j:
                    if dp1[j][i][n] < 0:
                        flag = 1
                        break
            if not flag:
                return i
    for i in range(-1, mask, -1):
        mask >>= 1
    return i

def getmask(mask, x, n):
    ans = 1 << x
    for i in range(n):
        if ((1 << i) & mask) and dp1[x][i][n] < 0:
            ans |= 1 << i
    return ans

n, m = map(int, input().split())
table = [[INF for _ in range(13)] for _ in range(13)]
dp1 = [[[0 for _ in range(14)] for _ in range(13)] for _ in range(13)]
dp2 = [None] * 9000
dp3 = [[0 for _ in range(10)] for _ in range(9000)]

for i in range(13):
    for j in range(13):
        table[i][j] = INF

for i in range(m):
    x, y = map(int, input().split())
    if x != y:
        table[x][y] = -1

for i in range(n):
    for j in range(n):
        dp1[i][j][0] = table[i][j]

for k in range(1, n+1):
    for i in range(n):
        for j in range(n):
            dp1[i][j][k] = min(dp1[i][j][k-1], dp1[i][k-1][k-1] + dp1[k-1][j][k-1])

t = list(0)
dp2[0] = t

for i in range(1, 1 << n):
    x = findleft(i, n)
    dp2[i] = dp2[i ^ (1 << x)]
    x = getmask(i, x, n)
    cur = dp2[i ^ x]
    while cur:
        t = list(x | cur.mask)
        t.next = dp2[i]
        dp2[i] = t
        cur = cur.next

for i in range(1 << n):
    dp3[i][0] = 1

for i in range(1, 10):
    for j in range(1 << n):
        dp3[j][i] = 0
        cur = dp2[j]
        while cur:
            dp3[j][i] = (dp3[j][i] + dp3[cur.mask][i-1]) % MOD
            cur = cur.next

print(dp3[(1 << n) - 1][9])