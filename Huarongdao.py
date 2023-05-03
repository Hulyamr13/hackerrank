import heapq
from collections import namedtuple


def h1(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def astar(table, x1, y1, x2, y2):
    ''' distance from x1 y1 to x2 y2 '''
    n, m = len(table), len(table[0])
    q = [(h1(x1, y1, x2, y2), 0, x1, y1)]
    saw = set()
    while q:
        _, steps, x, y = heapq.heappop(q)
        if (x, y) in saw:
            continue
        else:
            saw.add((x, y))
        if x == x2 and y == y2:
            return steps
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            tx, ty = x + i, y + j
            if 0 < tx <= n and 0 < ty <= m and table[tx - 1][ty - 1] == 1:
                heapq.heappush(q, (h1(tx, ty, x2, y2) + steps + 1, steps + 1, tx, ty))
    return -1


Status = namedtuple('status', 'hu steps sx sy ex ey')


def solve(table, k, ex, ey, sx, sy, tx, ty):
    n, m = len(table), len(table[0])
    hu = astar(table, sx, sy, tx, ty)
    if hu == -1:
        return -1
    init_status = Status(hu * (k + 1), 0, sx, sy, ex, ey)
    q = [init_status]
    saw = {}
    best = 1e7
    while q:
        st = heapq.heappop(q)
        if st[2:4] in saw and saw[st[2:4]] < st.steps:
            continue
        else:
            saw[st[2:4]] = st.steps
        if st.steps >= best:
            continue
        if st.sx == tx and st.sy == ty:
            if st.steps < best:
                best = st.steps

        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = st.sx + i, st.sy + j
            if 0 < nx <= n and 0 < ny <= m and table[nx - 1][ny - 1] == 1:

                table[st.sx - 1][st.sy - 1] = 0
                e2n = astar(table, st.ex, st.ey, nx, ny)
                table[st.sx - 1][st.sy - 1] = 1

                new_hu = (k + 1) * astar(table, nx, ny, tx, ty)

                if e2n == -1 or e2n > k:
                    new_steps = k + 1
                else:
                    new_steps = e2n + 1

                heapq.heappush(q, Status(st.steps + new_steps + new_hu, st.steps + new_steps,
                                         nx, ny, st.sx, st.sy))
    return best


def main():
    n, m, k, q = map(int, input().split())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    for i in range(q):
        ex, ey, sx, sy, tx, ty = map(int, input().split())
        print(solve(table, k, ex, ey, sx, sy, tx, ty))

main()