import math

Pi = 4 * math.atan(1.0)


def check_e0(x1, y1, x2, y2):
    return (x1 * y2 == x2 * y1) and (x1 * x2 >= 0) and (y1 * y2 >= 0)


def check_le90(x1, y1, x2, y2):
    return ((x1 * x2 + y1 * y2) >= 0) and (x1 * y2 - x2 * y1 < 0)


def get_angle(x, y):
    return math.atan2(x, y)


N = int(input())
vp = [tuple(map(int, input().split())) for _ in range(N)]
vc = [[0] * N for _ in range(N)]

for i in range(N):
    x, y = vp[i]
    va = [(get_angle(vp[j][1] - y, vp[j][0] - x), j) if i != j else (-2 * Pi, j) for j in range(N)]
    va.sort(reverse=True)

    j1, j2, j3 = 0, 1, 0
    while j1 < N - 1:
        if j2 == j1:
            j2 += 1
        while j2 < N - 1 and check_e0(vp[va[j1][1]][0] - x, vp[va[j1][1]][1] - y, vp[va[j2][1]][0] - x,
                                      vp[va[j2][1]][1] - y):
            j2 += 1
        j3 = max(j2, j3)
        while j3 < j1 + N - 1 and check_le90(vp[va[j1][1]][0] - x, vp[va[j1][1]][1] - y, vp[va[j3 % (N - 1)][1]][0] - x,
                                             vp[va[j3 % (N - 1)][1]][1] - y):
            j3 += 1
        vc[i][va[j1][1]] = j3 - j2
        j1 += 1

total = sum(vc[i][j] * vc[j][i] for i in range(N) for j in range(i + 1, N))
print(total)
