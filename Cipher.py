N, K = map(int, input().split())
S = list(map(int, input().strip()))
L = len(S)
Pre = [0 for _ in range(L)]
Pre[0] = S[0]
for i in range(1, L):
    Pre[i] = S[i - 1] ^ S[i]
    if i >= K:
        Pre[i] ^= Pre[i - K]
ans = ""
for i in range(0, L - K + 1):
    v = Pre[i]
    ans += "1" if v == 1 else "0"
print(ans)