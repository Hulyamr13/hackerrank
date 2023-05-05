from heapq import (
    heapify,
    heappush,
    heappop,
)

from math import inf


def full_dijkstra(nodes, source, type_tag):
    out = [-1 for _ in nodes]
    p_queue = []
    visit_history = []  # little hack
    heappush(p_queue, (0, source))

    while p_queue:
        weight, actual = heappop(p_queue)
        if type_tag in nodes[actual][1]:
            continue
        nodes[actual][1][type_tag] = weight
        out[actual] = weight
        visit_history.append(actual)

        for neighbor, length in nodes[actual][0]:
            if not type_tag in nodes[neighbor][1]:
                heappush(p_queue, (weight+length, neighbor))
    return visit_history, out


lista = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []

def run(n, m, k, edges):
    nodes = [([], {}) for _ in range(n+1)]  # indexed from 1 to n
    for a, b, c in edges:
        nodes[a][0].append((b, c))
        nodes[b][0].append((a, c))

    a, b, k_dis = edges[k-1]
    lista5.append(k_dis)

    historyA, distancesA = full_dijkstra(nodes, a, "A")
    historyB, distancesB = full_dijkstra(nodes, b, "B")

    pairs = list(zip(distancesA, distancesB))[1:]

    distB = distancesB
    distA = distancesA
    peaks = []
    C = k_dis
    N = n

    for da, db in zip(distA[1:], distB[1:]):
        point_delta = db-da # desde b hacia a, negativo es bueno
        x = (k_dis + point_delta) / 2 # normalized
        peaks.append((x, da + x))
    peaks.sort()

    pts = []
    for x, y in peaks: # costo1, costo2
        while pts:
            x0, y0 = pts[-1] # tomar el último elemento
            if y0 > y - x + x0: # y0 distancia punto anterior de B con respecto a P
                # (y - x) -> delta distancia actual
                # x0 + delta < y0 -> el punto B está más alejado de P
                break
            pts.pop()
        if pts:
            x0, y0 = pts[-1] # mismo que el del while
            xy = x0 + y0 # (2x + distA[i])
            if y > xy - x: # (dist b) > (2x + distA[i]) - distA
                x1 = (xy - y + x) / 2
                pts.append((x1, xy - x1)) # mori
                pts.append((x, y)) #
        else:
            if x > 0:
                pts.append((0, y - x)) # (x, y) -> (0, delta), diferencia entre los dos caminos mas largos
            pts.append((x, y)) # agregar el punto actual
    x, y = pts[-1]
    if x < C:
        pts.append((C, y + x - C))
    print("%.5f %.5f" % min(pts, key=lambda x: x[1]))


def official_run():
    t = int(input())
    for i in range(t):
        n, m, k = map(int, input().split(" "))
        # edge: A, B, C
        edges = [tuple(map(int, input().split(" ")))
                for _ in range(m)]
        run(n, m, k, edges)

#test_case_run()

official_run()