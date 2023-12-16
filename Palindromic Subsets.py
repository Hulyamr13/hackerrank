mod = 10 ** 9 + 7

polys = [1]
maxLen = 100


def updateDegree(e):
    while (len(polys) <= e):
        polys.append((polys[-1] * 2) % mod)


def getMask(l, r):
    mask = [0] * 26
    for i in range(l, r):
        mask[arr[i]] = 1
    return mask


def add(l, r, d):
    if ((d % 26) == 0) or (l == 0 and len(arr) == r):
        return
    for i in range(l, r):
        arr[i] = (arr[i] + d) % 26


class Node():
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.off = 0
        if (r - l) < maxLen:
            self.left = self.right = None
        else:
            mid = (r + l) // 2
            self.left = Node(self.l, mid)
            self.right = Node(mid, self.r)
        self.mask = None

    def add(self, l, r, off):
        if self.r < l or r < self.l:
            return
        l = max(l, self.l)
        r = min(r, self.r)
        if l == r or off == 0:
            return
        if l == self.l and r == self.r and self.left is not None:
            self.off += off
            self.off %= 26
            return

        if self.left is None:
            add(l, r, off)
            self.mask = None
        else:
            self.left.add(l, r, off)
            self.right.add(l, r, off)

    def getMask(self, l, r):
        if self.r < l or r < self.l:
            return [0] * 26
        l = max(l, self.l)
        r = min(r, self.r)
        if self.left:
            lmask = self.left.getMask(l, r)
            if all(lmask):
                return lmask
            rmask = self.right.getMask(l, r)
            if all(rmask):
                return rmask
            res = [0] * 26
            for i in range(26):
                res[(i + self.off) % 26] = rmask[i] or lmask[i]
            return res
        if self.l == l and self.r == r:
            if self.mask is None:
                self.mask = getMask(l, r)
            if self.off:
                res = [0] * 26
                for i in range(26):
                    res[(i + self.off) % 26] = self.mask[i]
            else:
                res = self.mask
            return res
        return getMask(l, r)

    def countPolyndroms(self, l, r):
        mask = self.getMask(l, r)
        counter = sum(mask)
        deg = r - l - counter

        updateDegree(deg)
        res = (counter + 1) * polys[deg] - 1
        return res % mod


n, Q = map(int, input().strip().split(' '))
s = input().strip()

arr = [ord(a) - ord('a') for a in s]
root = Node(0, len(arr))
for _ in range(Q):
    q = list(map(int, input().strip().split(' ')))
    q[2] += 1
    if q[0] == 1:
        root.add(*q[1:])
    else:
        print(root.countPolyndroms(*q[1:]))
