cumsum = []
res = []


def mn(ceil, beans):
    return (beans // ceil) * cumsum[ceil] + cumsum[beans % ceil]


def mx(ceil, beans):
    return cumsum[1] * beans


fmemo = set()


def f(ceil, sm, beans):
    if not (mn(ceil, beans) <= sm <= mx(ceil, beans)):
        return False
    if beans == 0 and sm == 0:
        return True
    if (ceil, sm, beans) in fmemo:
        return False

    for k in range(1, min(beans, ceil) + 1):
        if f(k, sm - cumsum[k], beans - k):
            res.append(k)
            return True
    fmemo.add((ceil, sm, beans))
    return False


for _ in range(int(input())):
    n, s, k = map(int, input().split())
    if n == 1:
        if k == 0:
            print(s)
        else:
            print(-1)
        continue
    if s == 0:
        if k == 0:
            print(' '.join(map(str, [0 for _ in range(n)])))
        else:
            print(-1)
        continue

    cumsum = [0, 2 * n - 2]
    for i in range(1, n):
        cumsum.append(cumsum[-1] + 2 * n - 2 - 2 * i)
    res = []
    f(n, k + (n - 1) * s, s)
    if res:
        r = [0 for _ in range(n)]
        for num in res:
            for i in range(num):
                r[-1 - i] += 1
        print(' '.join(map(str, r)))
    else:
        print(-1)