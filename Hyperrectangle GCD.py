MOD = 1000000007

def solve():
    n = int(input())
    lens = list(map(int, input().split()))
    f = [0] * (100000 + 10)

    m = 0
    for k in range(1, 100000 + 11):
        cnt = 1
        for i in range(n):
            cnt = (cnt * (lens[i] // k)) % MOD
        if cnt == 0:
            break
        f[k] = cnt
        m = k

    ans = 0
    for k in range(m, 0, -1):
        for i in range(k + k, m + 1, k):
            f[k] = (f[k] - f[i] + MOD) % MOD
        ans = (ans + k * f[k]) % MOD

    print(ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
