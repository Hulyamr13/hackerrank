n = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    op, m = input().split()
    B = set(map(int, input().split()))
    getattr(A, op)(B)

print(sum(A))