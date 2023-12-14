import bisect
from collections import defaultdict

N, Q, _ = map(int, input().split())
a = defaultdict(list)
y = list()
for _ in range(N):
    _, y_, freq = map(int, input().split())
    a[freq].append(y_)
    y.append(y_)

a = {freq: sorted(y) for freq, y in a.items() if len(y) > 1}
y = sorted(y)

res = []
for _ in range(Q):
    y_max, y_min, T = map(int, input().split())
    lres = 0
    index_start = bisect.bisect_left(y, y_min)
    if y[index_start] <= y_max:
        lres = 1
        for freq in a:
            index_start = bisect.bisect_left(a[freq], y_min)
            index_stop = bisect.bisect_right(a[freq], y_max)
            lres = max(lres, index_stop - index_start)
    res.append(lres)
print(*res, sep='\n')