mod = 1000000007

n = int(input())
arr = list(map(int, input().split()))

set1 = set(arr)
set2 = set1.copy()
count = 0

while set2:
    count += 1
    cur = min(set2)
    set2.remove(cur)
    while cur + 1 in set2:
        cur += 1
        set2.remove(cur)

q = int(input())
ans = 0

for i in range(q):
    id, val = map(int, input().split())
    id -= 1
    count -= 1

    curr = arr.count(arr[id])
    prev = arr.count(arr[id] - 1)
    next_val = arr.count(arr[id] + 1)

    if prev == 0 and next_val == 0:
        count += 1
    elif curr > max(prev, next_val):
        count += 1
    elif curr <= min(prev, next_val):
        count -= 1

    arr[id] = val

    curr = arr.count(arr[id])
    prev = arr.count(arr[id] - 1)
    next_val = arr.count(arr[id] + 1)

    if prev == 0 and next_val == 0:
        count -= 1
    elif (curr + 1) > max(prev, next_val):
        count -= 1
    elif (curr + 1) <= min(prev, next_val):
        count += 1

    ans = (ans + ((i + 1) * count) % mod) % mod

print(ans)
