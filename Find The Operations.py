def gauss(n, a, b):
    for i in range(n):
        row = -1
        for j in range(i, n):
            if a[j][i]:
                row = j
                break

        if row == -1:
            continue

        if not a[i][i]:
            for j in range(n + 1):
                a[i][j] ^= a[row][j]

        for k in range(i, n):
            if k != i and a[k][i] == 1:
                for j in range(n + 1):
                    a[k][j] ^= a[i][j]

    for i in range(n):
        if a[i][n]:
            ok = 0
            for j in range(n):
                if a[i][j]:
                    ok = 1
                    break
            if not ok:
                return 0

    for i in range(n - 1, -1, -1):
        if a[i][i] == 0 and a[i][n] == 1:
            return 0
        if a[i][i] == 0:
            b[i] = 0
        else:
            b[i] = a[i][n]

        if b[i]:
            for j in range(i - 1, -1, -1):
                if a[j][i] == 1:
                    a[j][n] ^= 1

    return 1


def main():
    n, d = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]

    a = [[0] * (n * n + 1) for _ in range(n * n)]
    root = [0] * (n * n)

    for i in range(n):
        for j in range(n):
            row = i * n + j
            a[row][n * n] = g[i][j]
            for x in range(n):
                for y in range(n):
                    if abs(x - i) + abs(y - j) <= d:
                        a[row][x * n + y] = 1

    res = gauss(n * n, a, root)

    if not res:
        print("Impossible")
    else:
        print("Possible")
        cnt = sum(root)
        print(cnt)
        for i in range(n * n):
            if root[i]:
                print(i // n, i % n)


if __name__ == "__main__":
    main()
