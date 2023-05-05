from typing import List

N = 600
MOD = 1000000007
nim = [0] * (N + 1)
mx = [0] * (N + 1)
mex = [0] * N
s = [[[0] * N for j in range(N + 1)] for i in range(2)]

def main() -> None:
    global nim, mx, mex, s
    n, m, x = map(int, input().split())
    if x == 2:
        for i in range(2, n + 1):
            nim[i] = (i & 1) ^ 1
    elif x == 3:
        tick = 0
        for i in range(2, n + 1):
            tick += 1
            for j in range(1, i):
                t = nim[j] ^ nim[i - j]
                if t < i:
                    mex[t] = tick
            for j in range(1, i):
                for k in range(1, i - j):
                    t = nim[j] ^ nim[k] ^ nim[i - j - k]
                    if t < i:
                        mex[t] = tick
            while mex[nim[i]] == tick:
                nim[i] += 1
    else:
        for i in range(2, n + 1):
            nim[i] = i - 1
    for i in range(2, n + 1):
        mx[i] = 0
        for j in range(1, i + 1):
            mx[i] = max(mx[i], mx[i - j] ^ nim[j])
    s[0][0][0] = 1
    for i in range(m):
        for j in range(n + 1):
            s[(i + 1) & 1][j] = [0] * N
        for j in range(n):
            for k in range(mx[j] + 1):
                if s[i & 1][j][k]:
                    for jj in range(1, n - j + 1):
                        kk = k ^ nim[jj]
                        if kk < N:
                            t = s[(i + 1) & 1][j + jj][kk]
                            t += s[i & 1][j][k]
                            if t >= MOD:
                                t -= MOD
                            s[(i + 1) & 1][j + jj][kk] = t
    print(sum(s[m & 1][n][1:]) % MOD)

if __name__ == "__main__":
    main()
