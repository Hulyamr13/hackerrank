def sol(a, b, c, d):
    global eng
    path[eng + 1] = vertical[a]
    vertical[a] = eng + 1
    V[eng + 1] = b
    land[eng + 1] = c
    hum[eng + 1] = d
    eng += 1


def dfs(x):
    global lq
    sand[x] = True
    i = vertical[x]
    while i > 0:
        if land[i]:
            if dig[x] + hum[i] < dig[V[i]]:
                dig[V[i]] = dig[x] + hum[i]
                few[V[i]] = i
                if not sand[V[i]]:
                    if dfs(V[i]):
                        return True
                else:
                    lq = V[i]
                    return True
        i = path[i]
    sand[x] = False
    return False


def fi():
    for i in range(1, num + 1):
        snow[i] = False
        dig[i] = 0
        sand[i] = False
    for i in range(1, num + 1):
        if not snow[i] and dfs(i):
            return i
    return 0


T = int(input())
while T > 0:
    T -= 1
    num, num1 = map(int, input().split())
    eng = 1
    vertical = [0] * 2100000
    path = [0] * 2100000
    V = [0] * 2100000
    few = [0] * 2100000
    hum = [0] * 2100000
    land = [0] * 2100000
    snow = [False] * 2100000
    sand = [False] * 2100000
    dig = [0] * 2100000
    for i in range(1, num):
        ss, dd, h = map(int, input().split())
        sol(ss, dd, h, 0)
        sol(dd, ss, h, 0)
    ans = 0
    for i in range(1, num1 + 1):
        ss, dd, h = map(int, input().split())
        sol(dd, ss, 1, -h)
        sol(ss, dd, 0, h)
    while fi() > 0:
        i = few[lq]
        while True:
            ans -= hum[i]
            land[i] -= 1
            land[i ^ 1] += 1
            if V[i ^ 1] == lq:
                break
            i = few[V[i ^ 1]]
    print(ans)
