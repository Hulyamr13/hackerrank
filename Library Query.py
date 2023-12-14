class FenwickTree2D:
    def __init__(self, x, y):
        self.size_x = x
        self.size_y = y
        self.data = [[0] * self.size_y for _ in range(self.size_x)]

    def sum(self, x1, y1):
        if min(x1, y1) <= 0: return 0
        s = 0
        x = x1
        while x >= 0:
            y = y1
            while y >= 0:
                s += self.data[x][y]
                y = (y & (y + 1)) - 1
            x = (x & (x + 1)) - 1
        return s

    def sumrange(self, x1, y1, x2, y2):
        return self.sum(x2, y2) \
            - self.sum(x1 - 1, y2) - self.sum(x2, y1 - 1) \
            + self.sum(x1 - 1, y1 - 1)

    def add(self, x1, y1, w):
        assert min(x1, y1) > 0
        x = x1
        while x < self.size_x:
            y = y1
            while y < self.size_y:
                self.data[x][y] += w
                y |= y + 1
            x |= x + 1


for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    t = FenwickTree2D(10001, 1001)
    for i in range(len(arr)):
        t.add(i + 1, arr[i], 1)
    Q = int(input())
    for q in range(Q):
        c = list(map(int, input().split()))
        if c[0] == 1:
            t.add(c[1], arr[c[1] - 1], -1)
            arr[c[1] - 1] = c[2]
            t.add(c[1], arr[c[1] - 1], 1)
        else:
            def select(l, r, k):
                lo, hi = 1, 1000
                while lo < hi:
                    med = (hi + lo) // 2
                    a = t.sumrange(l, 0, r, med)
                    if a >= k:
                        hi = med
                    else:
                        lo = med + 1

                if not t.sumrange(l, 0, r, lo) >= k:
                    raise ValueError
                return lo


            print(select(c[1], c[2], c[3]))