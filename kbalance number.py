N = 0
F = {}
G = {}

def f(k, n, i, s):
    if i == k:
        c, ss = g(k, n, 0, s, 0)
        C = c * 10 ** (n - 2 * k)
        S = ss * 10 ** (n - 2 * k) + c * 10 ** (n - 2 * k) * (10 ** (n - 2 * k) - 1) // 2 * 10 ** k
        return C % 1000000007, S % 1000000007
    if (i, s) not in F:
        C = 0
        S = 0
        for j in range(10):
            c, ss = f(k, n, i + 1, s + j)
            C += c
            S += ss + j * 10 ** (n - i - 1) * c
        F[i, s] = C % 1000000007, S % 1000000007
    return F[i, s]

def g(k, n, i, s1, s2):
    if s1 < s2:
        return 0, 0
    if i == k:
        return s1 == s2, 0
    if (i, s1, s2) not in G:
        C = 0
        S = 0
        for j in range(10):
            c, s = g(k, n, i + 1, s1, s2 + j)
            C += c
            S += s + j * 10 ** (k - i - 1) * c
        G[i, s1, s2] = C % 1000000007, S % 1000000007
    return G[i, s1, s2]

def calculate_k_balanced(L, R, K):
    def S(K, n, p):
        global N
        if N != n:
            N = n
            F.clear()
            G.clear()
        k = max(min(K, n - K), 0)
        P = int(''.join(map(str, p)))
        if len(p) <= k:
            c, s = f(k, n, len(p), sum(p))
        elif len(p) <= n - k:
            c, s = g(k, n, 0, sum(p[:k]), 0)
            s = s * 10 ** (n - k - len(p)) + c * 10 ** (n - k - len(p)) * (10 ** (n - k - len(p)) - 1) // 2 * 10 ** k
            c = c * 10 ** (n - k - len(p))
        else:
            c, s = g(k, n, k - n + len(p), sum(p[:k]), sum(p[n - k:]))
        return s + c * P * 10 ** (n - len(p))

    def X(K, A):
        A = list(map(int, str(A)))
        x = sum(S(K, i, [j]) for i in range(1, len(A)) for j in range(1, 10))
        x += sum(S(K, len(A), [j]) for j in range(1, A[0]))
        x += sum(S(K, len(A), A[:i] + [j]) for i in range(1, len(A)) for j in range(0, A[i]))
        return x

    return (X(K, R + 1) - X(K, L)) % 1000000007

L, R, K = map(int, input().split())
result = calculate_k_balanced(L, R, K)

print(result)
