def number_list(t, test_cases):
    result = []

    for i in range(t):
        n, k = test_cases[i][0], test_cases[i][1]
        a = test_cases[i][2:]

        p, cnt, nb = 0, 0, 0
        b = [0] * 200000

        while p < n:
            if a[p] <= k:
                cnt += 1
            else:
                if cnt != 0:
                    b[nb] = cnt
                    nb += 1
                cnt = 0
            p += 1

        if cnt != 0:
            b[nb] = cnt
            nb += 1

        res = 0
        for j in range(nb):
            res += (b[j] + 1) * b[j] // 2

        res = n * (n + 1) // 2 - res
        result.append(res)

    return result

t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    elements = list(map(int, input().split()))
    test_cases.append([n, k] + elements)

results = number_list(t, test_cases)
for res in results:
    print(res)
