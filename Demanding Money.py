from collections import defaultdict as ddic

N, M = map(int, input().split())
C = [0] + list(map(int, input().split()))

G = ddic(set)
for _ in range(M):
    i, j = map(int, input().split())
    G[i].add(j)
    G[j].add(i)

memo = {frozenset(): (0, 1)}


def dp(S):
    if S in memo:
        return memo[S]
    m = min(S)
    T = S - {m}
    money, ways = dp(T)
    U = S - frozenset(G[m] | {m})
    money2, ways2 = dp(U)
    money2 += C[m]
    if money > money2:
        ans = money, ways
    elif money2 > money:
        ans = money2, ways2
    else:
        ans = money, ways + ways2
    memo[S] = ans
    return ans


ans, ct = dp(frozenset(range(1, N + 1)))
print(ans, ct)