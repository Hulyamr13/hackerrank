def count_pairs(n, k, x):
    x.sort()
    l = [0 for i in range(100001)]
    for i in x:
        l[i - 1] = 1
    x = []
    for i in range(100001):
        if l[i] == 1:
            x.append(i + 1)

    start = 0
    i = 0
    c = 1
    n = len(x)
    while i < n:
        if x[i] <= x[start] + k:
            i = i + 1
            continue
        else:
            s = i - 1
            while i < n and x[s] + k >= x[i]:
                i += 1
            start = i
            if i < n:
                c += 1

    return c


if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    x = list(map(int, input().strip().split(' ')))

    result = count_pairs(n, k, x)
    print(result)