def missileDefend(n, inp):
    p = sorted([(a+b, a-b) for a, b in inp])
    a = [y for x, y in p]
    d = []
    for x in a:
        low, high = -1, len(d)
        while high - low > 1:
            mid = (low + high) >> 1
            if d[mid] > x:
                low = mid
            else:
                high = mid
        if high == len(d):
            d.append(x)
        else:
            d[high] = x
    return len(d)


if __name__ == '__main__':
    n = int(input())
    inp = [tuple(map(int, input().split())) for i in range(n)]
    result = missileDefend(n, inp)
    print(result)
