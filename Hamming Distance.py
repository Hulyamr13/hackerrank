def rev(x):
    x = (x & 0xaaaaaaaaaaaaaaaa) >> 1 | (x & 0x5555555555555555) << 1
    x = (x & 0xcccccccccccccccc) >> 2 | (x & 0x3333333333333333) << 2
    x = (x & 0xf0f0f0f0f0f0f0f0) >> 4 | (x & 0x0f0f0f0f0f0f0f0f) << 4
    x = (x & 0xff00ff00ff00ff00) >> 8 | (x & 0x00ff00ff00ff00ff) << 8
    x = (x & 0xffff0000ffff0000) >> 16 | (x & 0x0000ffff0000ffff) << 16
    return x >> 32 | x << 32

class BitSet:
    def __init__(self):
        self.N = 50000
        self.NN = (self.N + 63) // 64
        self.a = [0] * self.NN

    def flip(self, i):
        self.a[i >> 6] ^= 1 << (i & 63)

    def get(self, i):
        return (self.a[i >> 6] >> (i & 63)) & 1

    def set_bit(self, i, v):
        if self.get(i) != v:
            self.flip(i)

    def word(self, i, w):
        j = i >> 6
        self.a[j] |= w << (i & 63)
        i += 63
        j = i >> 6
        if j < self.NN:
            self.a[j] |= w >> 63 - (i & 63)

    def shr(self, i):
        ret = BitSet()
        o = i & 63
        shift = i // 64
        if not o:
            for i in range(self.NN - shift):
                ret.a[i] = self.a[i + shift]
        else:
            for i in range(self.NN - shift - 1):
                ret.a[i] = self.a[i + shift] >> o | self.a[i + shift + 1] << 64 - o
            ret.a[self.NN - shift - 1] = self.a[self.NN - 1] >> o
        return ret

    def fill(self, l, r, v):
        for i in range(l, r):
            if i & 63 or i + 63 >= r:
                self.set_bit(i, v)
            else:
                self.a[i >> 6] = -1 if v else 0
                i += 64

    def copy(self, o, l, r, to):
        shift = to - l
        for i in range(l, r):
            if i & 63 or i + 63 >= r:
                self.set_bit(i + shift, o.get(i))
            else:
                self.word(i + shift, o.a[i >> 6])
                i += 64

    def reverse(self, l, r):
        t = self.a[:]
        self.fill(l, r, 0)
        for i in range(l, r):
            if i & 63 or i + 63 >= r:
                self.set_bit(r - 1 - (i - l), t[i])
            else:
                self.word(r - 64 - (i - l), rev(t[i >> 6]))
                i += 64

    def xor(self, o):
        ret = BitSet()
        for i in range(self.NN):
            ret.a[i] = self.a[i] ^ o.a[i]
        return ret

n = int(input())
a = input()
b = BitSet()
for i in range(n):
    if a[i] == 'b':
        b.flip(i)

m = int(input())
for _ in range(m):
    op, x, y = input().split()
    x, y = int(x) - 1, int(y)
    if op == 'C':
        op, c = input().split()
        b.fill(x, y, ord(c) - ord('a'))
    elif op == 'R':
        b.reverse(x, y)
    elif op == 'W':
        output = ''
        for i in range(x, y):
            output += 'a' + chr(ord('a') + b.get(i))
        print(output)
    elif op == 'S':
        xx, yy = map(int, input().split())
        t = b
        b.fill(x, yy, 0)
        b.copy(t, x, y, yy - (y - x))
        b.copy(t, y, xx, x + (yy - xx))
        b.copy(t, xx, yy, x)
    elif op == 'H':
        y -= 1
        if x > y:
            x, y = y, x
        z = int(input())
        pop = 0
        t = b.xor(b.shr(y - x))
        for i in range(x, x + z):
            if i & 63 or i + 63 >= x + z:
                pop += t.get(i)
            else:
                pop += bin(t.a[i >> 6]).count('1')
                i += 64
        print(pop)
