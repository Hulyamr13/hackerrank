t = int(input())
a = 1000000007

for _ in range(t):
    s = 0
    l, m, n = map(int, input().split())
    l %= a
    m %= a
    n %= a

    s = (((n - 1) * (l - 1)) % a + a) * 500000004 % a + \
        (((n - 1) * (m - 1)) % a + a) * 500000004 % a + \
        (((m - 1) * (l - 1)) % a + a) * 500000004 % a
    s %= a
    s = (s + m + l + n - 2) % a

    print(s)
