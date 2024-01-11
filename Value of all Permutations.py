# Enter your code here. Read input from STDIN. Print output to STDOUT

def binary_search(A, N, M):
    lo, hi = -1, N
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if A[mid] <= M:
            lo = mid
        else:
            hi = mid
    return hi

P = int(input())
N = int(input())
A = sorted(map(int, input().split()))
Q = int(input())
distinct_perms = k = 1

sums = [0] * (N + 1)
for i in range(1, N + 1):
    sums[i] = (sums[i - 1] + A[i - 1]) % P

for i in range(1, N):
    if A[i] != A[i - 1]:
        k = 0
    k += 1
    distinct_perms = distinct_perms * (i + 1) * pow(k, P - 2, P) % P

for i in range(Q):
    M = int(input())
    idx = binary_search(A, N, M)
    print((sums[idx] * distinct_perms * pow(N - idx + 1, P - 2, P)) % P)
