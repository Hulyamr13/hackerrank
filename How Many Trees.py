# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 10**9 + 7
MAXN = 10**6

fact = [1] + [0] * (MAXN)
for i in range(1, MAXN + 1):
    fact[i] = fact[i - 1] * i % MOD

comb = lambda n, k: 1 if k == 0 or k == n else fact[n] * pow(fact[k] * fact[n - k], MOD - 2, MOD) % MOD

T = lambda n, k: (sum(comb(n - k, i) * pow(-1, n - k - i, MOD) * pow(i, n - 2, MOD) % MOD for i in range(1, n - k + 1)) * comb(n, k)) % MOD

N, L = map(int, input().split())
print(T(N, L))
