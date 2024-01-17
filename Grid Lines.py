# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 1000000007

from math import gcd
from collections import Counter

def solve_k2(n, m, k):
    a = (n + 1) * (m + 1)
    b = (n - 1) * (m - 1)
    return (a * (a - 1) - b * (b - 1)) // 2 % MOD

def solve(n, m, k):
    def compute_combin(n):
        c = [[1] * (i + 1) for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD
        return c

    def f(n, m, k):
        counts = Counter()
        def g(n, m, u, v):
            ndu, mdv = n // u, m // v
            if ndu > mdv:
                n, m, u, v, ndu, mdv = m, n, v, u, mdv, ndu
            a = n % u + 1
            b = m - ndu * v + 1
            s = ab = a * b
            counts[ndu + 1] += 2 * s
            for i in range(1, ndu + 1):
                a, b = a + u, b + v
                ab1 = a * b
                c = ab1 - ab - s
                s += c
                ab = ab1
                counts[ndu + 1 - i] += c + c

        counts[n + 1] += m + 1
        counts[m + 1] += n + 1
        uv = [(u, v) for u in range(1, n // (k - 1) + 1)
            for v in range(1, m // (k - 1) + 1) if gcd(u, v) == 1]
        for u, v in uv:
            g(n, m, u, v)
        return sum(v * combin[l][k] for l, v in counts.items() if l >= k)

    if k == 2: return solve_k2(n, m, k)
    combin = compute_combin(max(n + 1, m + 1))
    return (f(n, m, k) - f(n - 2, m - 2, k)) % MOD

n, m, k = map(int, input().split())
result = solve(n, m, k)
print(result)
