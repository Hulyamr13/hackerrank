# Enter your code here. Read input from STDIN. Print output to STDOUT

N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * K
found = [[False] * ((100 * 100) + 1) for _ in range(K + 1)]
duplicates = [[False] * ((100 * 100) + 1) for _ in range(K + 1)]

found[0][0] = True

for i in range(N):
    for count in range(K, 0, -1):
        for j in range(len(found[count - 1])):
            if not found[count - 1][j]:
                continue
            sum_val = j + A[i]
            if duplicates[count - 1][j] or found[count][sum_val]:
                duplicates[count][sum_val] = found[count][sum_val] = True
            else:
                found[count][sum_val] = True

ans = 0
for i in range(len(found[K])):
    if found[K][i] and not duplicates[K][i]:
        ans += i

print(ans)
