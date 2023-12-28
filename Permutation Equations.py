MOD = 10 ** 9 + 7
maxN = 200000
maxK = 60

dp = [[0] * maxK for _ in range(maxN)]
fact = [0] * (maxN + 1)


def precalc():
    fact[0] = 1
    for n in range(1, maxN + 1):
        fact[n] = (n * fact[n - 1]) % MOD

    dp[0][0] = 1
    for n in range(1, maxN):
        for k in range(1, maxK):
            dp[n][k] = (dp[n - 1][k - 1] + (n - 1) * dp[n - 1][k]) % MOD


def calc(n, L, R):
    ans = 0
    if L <= 0 and 0 <= R:
        ans = (fact[n] + MOD - fact[n - 1]) % MOD

    for k in range(maxK):
        pw2 = 1 << k
        if L <= pw2 <= R:
            ans = (ans + dp[n - 1][k]) % MOD

    return ans


def main():
    precalc()
    T = int(input())
    for _ in range(T):
        n, L, R = map(int, input().split())
        ans = calc(n, L, R)
        print(ans)


if __name__ == "__main__":
    main()
