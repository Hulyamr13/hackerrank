n, m = map(int, input().split())
ans = 0
c = [['0' for _ in range(m + 2)] for _ in range(n + 2)]

for i in range(1, n + 1):
    row = input().strip()
    for j in range(1, m + 1):
        c[i][j] = row[j - 1]

for x in range(1, n + 1):
    for y in range(1, m + 1):
        r = 0
        while c[x + r][y] == 'G' and c[x - r][y] == 'G' and c[x][y + r] == 'G' and c[x][y - r] == 'G':
            c[x + r][y] = c[x - r][y] = c[x][y + r] = c[x][y - r] = 'g'
            for X in range(1, n + 1):
                for Y in range(1, m + 1):
                    R = 0
                    while c[X + R][Y] == 'G' and c[X - R][Y] == 'G' and c[X][Y + R] == 'G' and c[X][Y - R] == 'G':
                        ans = max(ans, (1 + 4 * r) * (1 + 4 * R))
                        R += 1
            r += 1

        r = 0
        while c[x + r][y] == 'g' and c[x - r][y] == 'g' and c[x][y + r] == 'g' and c[x][y - r] == 'g':
            c[x + r][y] = c[x - r][y] = c[x][y + r] = c[x][y - r] = 'G'
            r += 1

print(ans)