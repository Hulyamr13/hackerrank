P = 10**9+7
N = 100000

for _ in range(int(input())):
    n = int(input())
    ans = 0
    nn = min(n, N)
    K = 0

    for d in range(1, nn + 1):
        K = n // d
        ans += K * (K - 1) // 2 * d
        ans += (n % d) * K

    ans %= P

    if nn < n:
        dd = nn + 1
        for i in range(1, N + 1):
            dn = n // (i + 1)
            if dn * (i + 1) < n:
                dn += 1
            if dn > n:
                dn = n + 1
            if dn - 1 >= dd:
                ans += (dn - 1 + dd) * (dn - dd) // 2 * i
            if dn < dd:
                dn = dd
            if dn <= n:
                dnr = n - i * dn
                if dnr > 0:
                    rr = (dnr + i - 1) // i
                    ans += (dnr + dnr - (rr - 1) * i) * rr // 2 * i

    print((ans + n) % P)
