MAX = 30000
MOD = 100003

N = int(input())
A = list(map(int, input().split()))

sol = [0] * MAX
sol[0] = A[0]

for i in range(1, N):
    tmp = sol[0]
    sol[0] = (sol[0] + A[i]) % MOD
    for j in range(1, i + 1):
        tmp1 = sol[j]
        sol[j] = (sol[j] + (tmp * A[i]) % MOD) % MOD
        tmp = tmp1

Q = int(input())

for _ in range(Q):
    k = int(input())
    print(sol[k - 1])
