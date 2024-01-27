# Enter your code here. Read input from STDIN. Print output to STDOUT

def power_mod(n, k, p):
    r = 1
    while k > 0:
        if k & 1:
            r *= n
            r %= p
        n *= n
        n %= p
        k >>= 1
    return r

def S0(N, K, P):
    c = [1]
    inv = [0, 1]
    s = []
    for k in range(1, K + 1):
        inv.append(P - (P // (k + 1)) * inv[P % (k + 1)] % P)
    for k in range(K + 1):
        c = [x + y for x, y in zip([0] + c, c + [0])]
        r = power_mod(N + 1, k + 1, P) - 1
        if r < 0:
            r += P
        for i in range(k):
            r -= c[i] * s[i] % P
            if r < 0:
                r += P
        r *= inv[k + 1]
        r %= P
        s.append(r)
    return s[K]

def S(N, K, R, P):
    R %= P
    if R == 0:
        return 0
    elif R == 1:
        return S0(N, K, P)
    iR = power_mod(R - 1, P - 2, P)
    c = [1]
    s = []
    for k in range(K + 1):
        r = power_mod(N, k, P) * power_mod(R, N + 1, P)
        if k == 0:
            r -= R
        r %= P
        if r < 0:
            r += P
        for i in range(k):
            if (k - i) & 1:
                r = (r - c[i] * s[i]) % P
                if r < 0:
                    r += P
            else:
                r = (r + c[i] * s[i]) % P
        r *= iR
        r %= P
        s.append(r)
        c = [x + y for x, y in zip([0] + c, c + [0])]
    return s[K]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    r = int(input())
    print(S(n, k, r, 10**9 + 7))
