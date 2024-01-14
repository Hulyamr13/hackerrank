MOD = 10 ** 9 + 7

def inv(N, M):
    x, lastx, y, lasty = 0, 1, 1, 0
    a, b = N, M

    while b != 0:
        q = a // b
        t = a % b
        a = b
        b = t

        t = x
        x = lastx - q * x
        lastx = t

        t = y
        y = lasty - q * y
        lasty = t

    return (lastx + M) % M

def comb(n, k, fact, invfact):
    if k < 0 or k > n:
        return 0
    return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD

def exp(b, e):
    r = 1
    while e > 0:
        if e % 2 == 1:
            r = r * b % MOD
        b = b * b % MOD
        e >>= 1
    return r

def main():
    n, m, k = map(int, input().split())
    deg = (2 * k) // m

    fact = [0] * 100010
    invfact = [0] * 100010
    fact[0] = 1

    for i in range(1, len(fact)):
        fact[i] = fact[i - 1] * i % MOD

    invfact[len(fact) - 1] = inv(fact[len(fact) - 1], MOD)
    for i in range(len(invfact) - 2, -1, -1):
        invfact[i] = invfact[i + 1] * (i + 1) % MOD

    p = deg * inv(m, MOD) % MOD

    ans = 1
    for i in range(1, n):
        s = 0
        for j in range(1, (n - 1) // i + 1):
            x = (p + (n - j * i) * inv(j, MOD) % MOD * (1 - p + MOD)) % MOD
            x = x * comb(n - j * i - 1, j - 1, fact, invfact) % MOD
            x = x * exp(p, j * i) % MOD
            x = x * exp(1 - p + MOD, j - 1) % MOD
            x = x if j % 2 == 1 else (MOD - x)
            s = (s + x) % MOD
            ans = (ans + x) % MOD
    print(ans)

if __name__ == "__main__":
    main()
