n, k = map(int, input().strip().split())

for i in range(10, n + 1):
    if all(sorted(list(str(i))) == sorted(list(str(i * j))) for j in range(2, k + 1)):
        print(*[i * x for x in range(1, k + 1)])
