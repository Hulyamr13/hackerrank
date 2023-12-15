n = int(input().strip())
a = list(map(int, input().strip().split()))
b = [0 for i in range(n)]
for i in range(n):
    v = a[i]
    if 0 == v or v >= n - 1:
        continue
    i1 = i - v + 1
    i2 = i + 1
    if i1 < 0:
        i1 += n
    if i2 >= n:
        i2 -= n;
    b[i1] -= 1
    b[i2] += 1
result, mv, tmp = 0, 0, 0
for i in range(n):
    tmp += b[i]
    if 0 == i or tmp > mv:
        result = i
        mv = tmp
#print(b)
print(result + 1)