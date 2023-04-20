from itertools import islice, accumulate

MOD = 10 ** 9 + 7


def permcount(permlen, a, b):
    if any(x + 1 == y for c in map(sorted, (a, b)) for x, y in zip(c, c[1:])):
        return 0
    if set(a) & set(b):
        return 0
    goingup = [None] * permlen
    for c, low in ((a, True), (b, False)):
        for elt in c:
            elt -= 1
            if elt > 0:
                goingup[elt] = not low
            if elt < permlen - 1:
                goingup[elt + 1] = low
    count = [1]
    for i, inc in islice(enumerate(goingup), 1, permlen):
        if inc is None:
            count = [sum(count)] * (i + 1)
        elif inc:
            count = [0] + list(accumulate(count))
        else:
            count = list(reversed(list(accumulate(reversed(count))))) + [0]
        count = [elt % MOD for elt in count]
    return sum(count) % MOD


def readints():
    return [int(f) for f in input().split()]


permlen, alen, blen = readints()
a = readints()
b = readints()
assert len(a) == alen and len(b) == blen
print(permcount(permlen, a, b))