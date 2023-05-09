
class Super:
    def __init__(self, n):
        lenn = 1
        while lenn < n:
            lenn *= 2
        self.lenn = lenn
        self.maxi = [0] * (2 * lenn)
        self.extra = [0] * (2 * lenn)

    def addrange(self, r):
        r += self.lenn
        l = self.lenn
        update = []
        while r > l:
            if (r % 2) == 1:
                r -= 1
                self.extra[r] += 1
                update.append(r)
            r //= 2
            l //= 2
        for n in update:
            n //= 2
            maxx = max(self.maxi[2 * n] + self.extra[2 * n], self.maxi[2 * n + 1] + self.extra[2 * n + 1])
            while n > 0 and maxx > self.maxi[n]:
                self.maxi[n] = maxx
                n //= 2
                maxx = max(self.maxi[2 * n] + self.extra[2 * n], self.maxi[2 * n + 1] + self.extra[2 * n + 1])

    def setval(self, n, value):
        n += self.lenn
        self.extra[n] = value
        n //= 2
        maxx = max(self.maxi[2 * n] + self.extra[2 * n], self.maxi[2 * n + 1] + self.extra[2 * n + 1])
        while n > 0 and maxx > self.maxi[n]:
            self.maxi[n] = maxx
            n //= 2
            maxx = max(self.maxi[2 * n] + self.extra[2 * n], self.maxi[2 * n + 1] + self.extra[2 * n + 1])

    def maxii(self):
        return self.maxi[1] + self.extra[1]


q = int(input())
for _ in range(q):
    m, n = [int(x) for x in input().split()]
    cats = [[] for _ in range(m + 1)]
    dogs = [[] for _ in range(m + 1)]
    types = []
    starts = []
    ends = []
    for c in input().split():
        if c == 'E' or c == 'C':
            types.append(0)
        else:
            types.append(1)
    for c in input().split():
        starts.append(int(c))
    for c in input().split():
        ends.append(int(c))
    for i in range(n):
        if ends[i] < starts[i]:
            continue
        if types[i] == 0:
            cats[ends[i]].append(starts[i])
        else:
            dogs[ends[i]].append(starts[i])
    best = [0] * (m + 1)
    C = Super(m + 1)
    D = Super(m + 1)
    for j in range(1, m + 1):
        for start in cats[j]:
            C.addrange(start + 1)

        for start in dogs[j]:
            D.addrange(start + 1)

        cmaxi = C.maxii()
        dmaxi = D.maxii()
        C.setval(j, dmaxi)
        D.setval(j, cmaxi)

        best[j] = max(cmaxi, dmaxi, best[j - 1])
    goal = 1
    ind = 0
    outp = []

    while ind <= m:
        while ind <= m and best[ind] < goal:
            ind += 1
        while ind <= m and best[ind] >= goal:
            outp.append(ind)
            goal += 1
        ind += 1
    while goal < n + 1:
        goal += 1
        outp.append(-1)
    print(*outp)