MOD = 10**9 + 7
N = 100005

def inv(x, y, p, q, r, s):
    if y == 0:
        return (p % MOD + MOD) % MOD
    return inv(y, x % y, r, s, p - r * (x // y), q - s * (x // y))

def C(n, k, f, g):
    if n < k:
        return 0
    if k == 0 or n == k:
        return 1
    return f[n] * g[k] % MOD * g[n - k] % MOD

n, k = map(int, input().split())

f = [0] * (N)
g = [0] * (N)

f[0] = 1
for i in range(1, n + 1):
    f[i] = f[i - 1] * i % MOD

for i in range(1, n + 1):
    g[i] = inv(f[i], MOD, 1, 0, 0, 1)

a = list(map(int, input().split()))
a.sort()

ans = 0
for i in range(k, n + 1):
    ans += a[i - 1] * C(i - 1, k - 1, f, g) % MOD

for i in range(1, n - k + 2):
    ans -= a[i - 1] * C(n - i, k - 1, f, g) % MOD

ans = (ans % MOD + MOD) % MOD
print(ans)
