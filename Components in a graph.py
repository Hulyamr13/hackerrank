from collections import defaultdict

n = int(input())
A = defaultdict(lambda: [])
for _ in range(n):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

low = high = None

U = set(A)
S = set()
for u in U:
    if u not in S:
        i = 0
        V = [u]
        T = set()
        T.add(u)

        while i < len(V):
            v = V[i]
            S.add(v)
            i += 1
            for w in A[v]:
                if w not in T:
                    T.add(w)
                    V.append(w)

        if low is None or i < low:
            if i == 1:
                print("i", i, "S", S, "T", T, "u", u)
            low = i
        if high is None or i > high:
            high = i
print(low, high)