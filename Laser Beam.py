MOD = 1000000007
C = 2000000
Gs = [0] * (C + 1)
_G = {}

def cubic_remainder(n):
    n %= MOD
    return (n * n % MOD * n % MOD)

def sequence(n):
    global Gs, _G
    if n <= C:
        return Gs[n]
    if n not in _G:
        s = cubic_remainder(2 * n + 1) - 1
        sq = int(n ** 0.5)
        nsq = n // sq
        for j in range(2, nsq + 1):
            s -= sequence(n // j)
        s %= MOD
        pv = n
        for v in range(1, sq):
            nx = n // (v + 1)
            s -= Gs[v] * (pv - nx)
            s %= MOD
            pv = nx
        _G[n] = s
        return s
    return _G[n]

def calculate_sequence():
    global Gs
    Gs[0] = 2
    for n in range(1, C + 1):
        Gs[n] = (Gs[n - 1] + 48 * n - 24) % MOD
    Gs[0] = 0
    for n in range(1, C + 1):
        for j in range(n * 2, C + 1, n):
            Gs[j] -= Gs[n]
        Gs[n] += Gs[n - 1]
        Gs[n] %= MOD

def main():
    global Gs
    calculate_sequence()

    z = int(input())
    while z > 0:
        z -= 1
        n, m, d = map(int, input().split())

        c1, c2 = 0, 0
        m1d = (m - 1) // d
        if m1d + 1 <= n // d:
            sq = int(n ** 0.5)
            nsq = n // sq
            nsqd = nsq // d * d
            nsq1d = (nsq - 1) // d * d
            for q in range((m1d + 1) * d, nsq1d + 1, d):
                c1 += sequence(n // q)
                c2 += sequence(n // (q + 1))
            for q in range(max(m1d * d, nsq1d) + d, nsqd + 1, d):
                c1 += sequence(n // q)
            for v in range(1, sq):
                g = Gs[v]
                nv = n // v
                nv1 = n // (v + 1)
                up = nv // d
                dn = max(m1d, nv1 // d)
                if up > dn:
                    c1 += g * (up - dn)
                up = (nv - 1) // d
                dn = max(m1d, (nv1 - 1) // d)
                if up > dn:
                    c2 += g * (up - dn)
        c = (c1 - c2) % MOD
        if c < 0:
            c += MOD
        print(c)

if __name__ == "__main__":
    main()
