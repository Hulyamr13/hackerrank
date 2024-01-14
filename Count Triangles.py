import math
from collections import defaultdict

err = pow(10, -12)

t = int(input())
for _ in range(t):
    n = int(input())
    minang = math.pi / n
    s = input()
    blocked = []
    for i in range(n):
        if s[i] == '0':
            blocked.append(i)

    global numdiff
    numdiff = 0

    numars = 0
    for a in range(1, n // 3 + 1):
        numars += (n - a) // 2 + 1 - a

    diffar = set()

    triangarea = defaultdict(lambda: 6 * n)

    triangrep = dict()

    for a in range((n - 1) % 2 + 1, n, 2):
        b = (n - a) // 2
        c = b

        [alta, altb, altc] = sorted([a, b, c])
        area = round(math.sin(a * minang) * math.sin(b * minang) * math.sin(c * minang), 12)
        triangarea[(alta, altb, altc)] = 3 * n
        diffar.add((alta, altb, altc))

    if n % 4 == 0:
        for a in range(1, ((n + 4) // 8)):
            b = (n // 2) - 2 * a
            c = (n // 2) + a
            [diffa, diffb, diffc] = sorted([a, b, c])
            area = round(math.sin(a * minang) * math.sin(b * minang) * math.sin(c * minang), 12)
            triangarea[(diffa, diffb, diffc)] = 12 * n
            numars -= 1
            [alta, altb, altc] = sorted([(n // 4) - a, 3 * (n // 4) - a, 2 * a])
            triangrep[(alta, altb, altc)] = (diffa, diffb, diffc)
            diffar.add((diffa, diffb, diffc))

    if n % 30 == 0:
        area = round(math.sin(4 * math.pi / 30) * math.sin(12 * math.pi / 30) * math.sin(14 * math.pi / 30), 12)
        triangarea[(4 * n // 30, 12 * n // 30, 14 * n // 30)] = 12 * n
        numars -= 1
        triangrep[(6 * n // 30, 7 * n // 30, 17 * n // 30)] = (4 * n // 30, 12 * n // 30, 14 * n // 30)
        diffar.add((4 * n // 30, 12 * n // 30, 14 * n // 30))

        area = round(math.sin(1 * math.pi / 30) * math.sin(11 * math.pi / 30) * math.sin(18 * math.pi / 30), 12)
        triangarea[(1 * n // 30, 11 * n // 30, 18 * n // 30)] = 12 * n
        numars -= 1
        triangrep[(2 * n // 30, 6 * n // 30, 22 * n // 30)] = (1 * n // 30, 11 * n // 30, 18 * n // 30)
        diffar.add((1 * n // 30, 11 * n // 30, 18 * n // 30))

    if n % 24 == 0:
        area = 0.25
        triangarea[(3 * n // 24, 6 * n // 24, 15 * n // 24)] = 12 * n
        numars -= 1
        triangrep[(2 * n // 24, 10 * n // 24, 12 * n // 24)] = (3 * n // 24, 6 * n // 24, 15 * n // 24)
        diffar.add((3 * n // 24, 6 * n // 24, 15 * n // 24))

    if n % 12 == 0:
        area = round(math.sqrt(3) / 8, 12)
        triangarea[(1 * n // 12, 4 * n // 12, 7 * n // 12)] = 9 * n
        triangarea.pop((2 * n // 12, 2 * n // 12, 8 * n // 12))
        diffar.remove((2 * n // 12, 2 * n // 12, 8 * n // 12))
        diffar.add((1 * n // 12, 4 * n // 12, 7 * n // 12))

    if n % 3 == 0:
        area = round(math.sqrt(27) / 8, 12)
        triangarea[(n // 3, n // 3, n // 3)] = n
        diffar.add((n // 3, n // 3, n // 3))

    b = len(blocked)
    for i in range(b):
        x = blocked[i]
        for j in range(i):
            y = blocked[j]
            for k in range(j):
                z = blocked[k]
                a = (x - y) % n
                b = (y - z) % n
                c = (z - x) % n

                [a, b, c] = sorted([a, b, c])
                area = round(math.sin(a * minang) * math.sin(b * minang) * math.sin(c * minang), 12)
                try:
                    coords = triangrep[(a, b, c)]
                except:
                    coords = (a, b, c)
                triangarea[coords] -= 3
                diffar.add(coords)

    toprint = sum(map(lambda x: ((x // 3) * (x // 3 - 1)) // 2, triangarea.values()))
    toprint += (numars - len(diffar)) * ((n) * (2 * n - 1))
    print(toprint)