def init():
    c = [[0] * 21 for _ in range(21)]
    for i in range(1, 21):
        c[i][0] = c[i][i] = 1
        for j in range(1, i):
            c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
    return c


def lexicographic_paths(t, test_cases):
    c = init()
    result = []

    for i in range(t):
        n, m, k = test_cases[i]
        cx, cy = 0, 0
        path = ""

        while cx != n or cy != m:
            nH = n - cx
            nV = m - cy

            if nH == 0:
                path += "V"
                cy += 1
            elif nV == 0:
                path += "H"
                cx += 1
            else:
                temp = c[nH + nV - 1][nH - 1]
                if k >= temp and temp > 0:
                    path += "V"
                    k -= temp
                    cy += 1
                else:
                    path += "H"
                    cx += 1

        result.append(path)

    return result


t = int(input())
test_cases = []
for _ in range(t):
    n, m, k = map(int, input().split())
    test_cases.append((n, m, k))

paths = lexicographic_paths(t, test_cases)
for path in paths:
    print(path)
