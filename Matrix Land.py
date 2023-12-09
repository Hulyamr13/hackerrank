n, m = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

pre = [0] * m
cur = [0] * m
l = [0] * m
r = [0] * m

def get_cur(idx):
    for i in range(m):
        val = 0
        for j in range(i, -1, -1):
            l[i] = max(l[i], val)
            val += A[idx][j]
            val = max(val, 0)

    for i in range(m - 1, -1, -1):
        val = 0
        for j in range(i, m):
            r[i] = max(r[i], val)
            val += A[idx][j]
            val = max(val, 0)

    cur[0] = pre[0] + A[idx][0] + r[0]
    pre_max = pre[0]

    for i in range(1, m):
        sum_val = sum(A[idx][0:i + 1])
        use_pre = pre_max + sum_val + r[i]
        use_cur = l[i] + pre[i] + sum_val + r[i]
        cur[i] = max(use_pre, use_cur)
        pre_max = max(pre_max, pre[i] + l[i] - sum_val)

    cur[m - 1] = max(cur[m - 1], pre[m - 1] + A[idx][m - 1] + l[m - 1])
    pre_max = pre[m - 1]

    for i in range(m - 2, -1, -1):
        sum_val = sum(A[idx][i:m])
        use_pre = pre_max + sum_val + l[i]
        cur[i] = max(cur[i], use_pre)
        pre_max = max(pre_max, pre[i] + r[i] - sum_val)

def solve():
    get_cur(0)
    for i in range(1, n):
        pre, cur = cur, pre
        get_cur(i)

    ans = max(cur)
    print(ans)

solve()
