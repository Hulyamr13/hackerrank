I = lambda: map(int, input().split())
_ = input()
A = list(I())
Q = []

for i in range(20):
    x = [0]
    for a in A:
        x.append(x[-1] + (a & (1 << i) > 0))
    Q.append(x)

for _ in range(int(input())):
    K, P, R = I()
    res = 0

    for j in range(20):
        q = Q[j][R] - Q[j][P - 1]
        N = R - P + 1
        v = q * (N - q)

        if K & (1 << j):
            v = N * (N - 1) // 2 - v

        res += v << j

    print(res % (10**9 + 7))
