import math
import os
from functools import reduce

def max_bit(x):
    for i in range(31):
        if x == 1:
            return i
        x >>= 1
    return None

start = (2**16, 16)

def max_bit2(x):
    res = 0
    s, n = start
    while n > 0:
        if x >= s:
            x >>= n
            res += n
        n >>= 1
        s >>= n
    return res

class Basis:
    def __init__(self):
        self.source = {}
        self.basis = []

    def expand(self, x):
        res = tuple()
        for di, bi in self.basis:
            if (x >> di) & 1 > 0:
                x ^= bi
                res = (di, bi)
            if x == 0:
                break
        return x, res

    def update(self, x):
        return self.remove(-x) if x < 0 else self.add(x)

    def add(self, x):
        res, key = self.expand(x)

        if res != 0:
            key = (max_bit2(res), res)
            self.basis.append(key)
            self.source[key] = set()

        self.source[key].add(x)

        return self

    def remove(self, x):
        res, key = self.expand(x)
        assert res == 0, f"{x} was not in set"
        s = self.source[key]
        s.discard(x)

        if len(s) == 0:
            del self.source[key]
            i = self.basis.index(key)
            self.basis, rest = self.basis[:i], self.basis[i + 1:]
            source = self.source
            append = False
            for k in rest:
                if append:
                    self.basis.append(k)
                else:
                    src = source[k]
                    del source[k]
                    len_b = len(self.basis)
                    for x in src:
                        self.add(x)
                    append = len(self.basis) == len_b + 2

        return self

    def max_xor(self):
        return reduce(lambda res, item: res ^ item[1] if (res >> item[0]) & 1 == 0 else res, sorted(self.basis, reverse=True), 0)

    def __repr__(self):
        return f"set: {set.union(set(), *self.source.values())}\nmax_XOR: {self.max_xor()}"

def solve(a):
    b = Basis()
    return [b.update(x).max_xor() for x in a]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
