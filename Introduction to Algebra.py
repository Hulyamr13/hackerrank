def quasi(a):
    n = len(a)
    for x in range(n):
        for y in range(n):
            cnt = sum(1 for z in range(n) if a[x][z] == y)
            if cnt != 1:
                return False
            cnt = sum(1 for z in range(n) if a[z][x] == y)
            if cnt != 1:
                return False
    return True

def loop(a):
    n = len(a)
    ce = 0
    E = 0
    for e in range(n):
        cnt = sum(1 for x in range(n) if a[e][x] == x and a[x][e] == x)
        if cnt == n:
            ce += 1
            E = e
    return ce == 1, E

def semi(a):
    n = len(a)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if a[a[x][y]][z] != a[x][a[y][z]]:
                    return False
    return True

def group(a, E):
    n = len(a)
    for x in range(n):
        cnt = sum(1 for y in range(n) if a[x][y] == E and a[y][x] == E)
        if cnt == 0:
            return False
    return True

def abelian(a):
    n = len(a)
    for x in range(n):
        for y in range(n):
            if a[x][y] != a[y][x]:
                return False
    return True

def rack(a):
    n = len(a)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if a[x][a[y][z]] != a[a[x][y]][a[x][z]]:
                    return False
            cnt = sum(1 for z in range(n) if a[x][z] == y)
            if cnt != 1:
                return False
    return True

def quandle(a):
    n = len(a)
    return all(a[x][x] == x for x in range(n))

def check(a):
    sco = 0
    n = len(a)
    E = -1
    is_loop, E = loop(a)
    if quasi(a):
        sco += 1
        if is_loop:
            sco += 2
    if semi(a):
        sco += 4
        if is_loop:
            sco += 8
            if group(a, E):
                sco += 16
                if abelian(a):
                    sco += 32
    if rack(a):
        sco += 64
        if quandle(a):
            sco += 128
    return sco

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [list(map(int, input().split())) for _ in range(n)]
        print(check(a))
