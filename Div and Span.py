# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 10**9 + 7

def powmod(a, b):
    res = 1
    a %= MOD
    assert b >= 0
    while b:
        if b & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b >>= 1
    return res


N = 201000
fac = [0] * N
fnv = [0] * N
cat = [0] * N
dp = [[0] * 210 for _ in range(210)]

fac[0] = 1
fnv[0] = 1
for i in range(1, 200011):
    fac[i] = (fac[i - 1] * i) % MOD
    fnv[i] = powmod(fac[i], MOD - 2)

for i in range(1, 100001):
    cat[i] = (fac[2 * i] * fnv[i] % MOD * fnv[i + 1] % MOD)

dp[0][0] = 1
for i in range(1, 201):
    for j in range(1, 201):
        for k in range(1, j + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][j - k] * cat[k]) % MOD

cases = int(input())
for _ in range(cases):
    x, y = map(int, input().split())
    ret = 0
    for j in range(1, y + 1):
        ret = (ret + fac[2 * x + 1] * fnv[j] % MOD * fnv[2 * x + 1 - j] % MOD * dp[j][y]) % MOD
    ret = ret * cat[x] % MOD * fac[x] % MOD * fac[y] % MOD
    print(ret)