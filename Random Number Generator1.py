import math

N = 1000010
f = [0.0] * N

for i in range(1, N):
    f[i] = f[i-1] + 1.0 / i

def solve(n):
    if n == 1:
        print("0")
        return
    if n == 2:
        print("0.5")
        return

    l, r = 1, n
    while l <= r:
        m = (l + r) // 2
        if (n - m - 1) / (f[n] - f[m-1]) <= m:
            r = m - 1
        else:
            l = m + 1
    r += 1
    a = (n - r - 1) / (f[n] - f[r-1])
    m = 2 * n - 1
    ans = (n + r) / m * (n - r + 1) * 0.25 - a * 0.5 * a / m * (f[n] - f[r-1])
    print(f"{ans:.15f}")

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        solve(n)
