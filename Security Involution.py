def involution():
    n = int(input())
    values = list(map(int, input().split()))

    for i in range(n):
        if values[values[i] - 1] != i + 1:
            print('NO')
            return

    print('YES')

involution()
