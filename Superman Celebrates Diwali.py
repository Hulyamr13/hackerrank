def main():
    n, h, hl = map(int, input().split())
    cnt = [[0 for _ in range(1901)] for _ in range(1900)]
    f = [[0 for _ in range(1901)] for _ in range(1900)]
    g = [0 for _ in range(1901)]
    for ctr in range(n):
        lis = list(map(int, input().split()))
        for j in range(1, len(lis)):
            cnt[ctr][lis[j]] += 1
    for ctr in range(n):
        f[ctr][h] = cnt[ctr][h]
        if f[ctr][h] > g[h]:
            g[h] = f[ctr][h]
    for j in range(h - 1, -1, -1):
        for i in range(n):
            tmp = 0
            if j + hl <= h:
                if g[j + hl] > tmp:
                    tmp = g[j + hl]
            if f[i][j + 1] > tmp:
                tmp = f[i][j + 1]
            f[i][j] = tmp + cnt[i][j]
            if f[i][j] > g[j]:
                g[j] = f[i][j]
    ans = 0
    for ctr in range(n):
        ans = max(ans, f[ctr][0])
    print(ans)


if __name__ == '__main__':
    main()
