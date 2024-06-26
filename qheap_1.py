import heapq

try:
    input = raw_input
except:
    pass

def find_deleted(h, d):
    while True:
        x = h[0]
        if x in d:
            heapq.heappop(h)
            d[x] -= 1
            if d[x] <= 0:
                del d[x]
        else:
            break
    return x

d = {}
h = []
Q = int(input())
for q in range(Q):
    l = [int(x) for x in input().strip().split(' ')]
    (a, b) = (l[0], l[1] if len(l) > 1 else None)
    if a == 1:
        heapq.heappush(h, b)
    elif a == 2:  # mark for deletion
        if b in d:
            d[b] += 1
        else:
            d[b] = 1
    else:
        x = find_deleted(h, d)
        print(x)
