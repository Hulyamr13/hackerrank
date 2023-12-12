g = int(input().strip())
for a0 in range(g):
    n, m, s = map(int, input().strip().split(' '))
    n2 = (n * n - 3 * n + 4) // 2
    if n == 2:
        print(s)
    else:
        if m <= n2:
            print(s + m - n + 1)
        else:
            a1 = n2 + (s - n + 2) * (m - n2 + 1) - 1
            x = n - 1 - s % (n - 1)
            y = s % (n - 1)
            div = s // (n - 1)
            t = (x * (x + 1)) // 2
            a2 = t * div
            a2 += max(0, (div + 1) * (m - t))
            rem = s - (n - 2) * div
            kant = ((n - 2) * (n - 1)) // 2
            a3 = kant * div + (m - kant) * rem
            print(min(a1, a2, a3))