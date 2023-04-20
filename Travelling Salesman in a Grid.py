import os
import sys

#
# Complete the tspGrid function below.
#
INF = 10 ** 9

m = True, False, None
TT, TF, TN, FT, FF, FN, NT, NF, NN = ((i, j) for i in m for j in m)

m, n = map(int, input().split())
row = [list(map(int, input().split())) for i in range(m)]
column = [list(map(int, input().split())) for j in range(m - 1)]

def minimize(t, v):
    global current, INF
    current[t] = min(v, current.get(t, INF))

if m & n & 1:
    ans = 0
else:
    ans = INF
    previous, current = {}, {NN[:1] * (m + n): 0}
    for i in range(m):
        for j in range(n):
            previous, current, k = current, {}, m + j - 1 - i
            for state, value in previous.items():
                l, x, r = state[:k], state[k: k + 2], state[k + 2:]
                if x == NN:
                    if i + 1 < m and j + 1 < n:
                        minimize(l + TF + r, value)
                elif x == NT or x == NF:
                    value += column[i - 1][j]
                    if j + 1 < n:
                        minimize(state, value)
                    if i + 1 < m:
                        minimize(l + x[::-1] + r, value)
                elif x == FN or x == TN:
                    value += row[i][j - 1]
                    if j + 1 < n:
                        minimize(l + x[::-1] + r, value)
                    if i + 1 < m:
                        minimize(state, value)
                else:
                    value += row[i][j - 1] + column[i - 1][j]
                    if x == TF:
                        if i + 1 == m and j + 1 == n:
                            ans = min(ans, value)
                    elif x == FT:
                        minimize(l + NN + r, value)
                    elif x == TT:
                        count = 1
                        index = -1
                        while count:
                            index += 1
                            count += 1 if r[index] == TT[0] else -1 if r[index] == FF[0] else 0
                        minimize(l + NN + r[:index] + TT[:1] + r[index + 1:], value)
                    else:
                        count = -1
                        index = k
                        while count:
                            index -= 1
                            count += 1 if l[index] == TT[0] else -1 if l[index] == FF[0] else 0
                        minimize(l[:index] + FF[:1] + l[index + 1:] + NN + r, value)
print(ans)