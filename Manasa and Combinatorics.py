MOD = 99991

def factMod(n):
    res = 1
    while n > 0:
        lt = n % MOD
        for num in range(2, lt + 1):
            res = (res * num) % MOD
        if (n // MOD) % 2:
            res = MOD - res
        n = n // MOD
    return res

def fastpow(a, n, temp):
    if n == 0:
        return 1
    if n == 1:
        return (a * temp) % MOD
    if n % 2:
        temp = (temp * a) % MOD
    return fastpow((a * a) % MOD, n // 2, temp)

def countF(n, p):
    cnt = 0
    while p <= n:
        cnt = cnt + n // p
        p = p * p
    return cnt

def C(n, r):
    if countF(n, MOD) > countF(n - r, MOD) + countF(r, MOD):
        return 0
    return factMod(n) * fastpow(factMod(n - r), MOD - 2, 1) * fastpow(factMod(r), MOD - 2, 1)

t = int(input())
for cases in range(t):
    n = int(input())
    ans = C(3 * n, n)
    ans = ans % MOD
    ans = ans * fastpow(n + 1, MOD - 2, 1)
    ans = (ans * fastpow(2 * n + 1, MOD - 2, 1)) % MOD
    ans = ans * ((n * (n + 1)) // 2 + 1)
    print(ans % MOD)
