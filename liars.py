import os
import sys

def get(n, limits):
    edges = []
    v = n + 1

    for x in range(n):
        temp1 = [x + 1, x, 0]
        temp2 = [x, x + 1, 1]
        edges.append(temp1)
        edges.append(temp2)

    for x in range(n + 1):
        temp1 = [v, x, 0]
        edges.append(temp1)

    for limit in limits:
        temp1 = [limit[0] - 1, limit[1], limit[2]]
        temp2 = [limit[1], limit[0] - 1, -limit[2]]
        edges.append(temp1)
        edges.append(temp2)

    dist = [10**9] * (n + 2)
    dist[v] = 0

    for x in range(n + 1):
        for i in range(len(edges)):
            dist[edges[i][1]] = min(dist[edges[i][1]], dist[edges[i][0]] + edges[i][2])

    return dist[n] - dist[0]


def liars(n, sets):
    rev = []

    for s in sets:
        temp = s[1] - s[0] + 1 - s[2]
        tmp1 = [s[0], s[1], temp]
        rev.append(tmp1)

    ret = [get(n, sets), n - get(n, rev)]
    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    sets = []
    for _ in range(m):
        sets.append(list(map(int, input().split())))

    result = liars(n, sets)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
