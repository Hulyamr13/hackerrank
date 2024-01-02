n = int(input())
a = list(map(int, input().split()))

sum_a = sum(a)
ans = sum((i + 1) * a[i] for i in range(n))

best = ans
for i in range(n):
    ans -= sum_a
    ans += n * a[i]
    best = max(best, ans)

print(best)
