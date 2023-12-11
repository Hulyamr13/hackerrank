import operator
from functools import reduce


def xor(nums):
    return reduce(operator.xor, nums, 0)


def lowZero(v):
    p = 0
    while True:
        m = 1 << p
        if v & m == 0:
            return p
        p += 1


def highOne(v):
    p = 0
    high = None
    while v != 0:
        m = 1 << p
        if v & m != 0:
            high = p
            v &= ~m
        p += 1
    return high


def zeroAt(v, p):
    return v & (1 << p) == 0


def diffToFlip(v, p):
    t = 1 << p
    r = (v + t) & ~(t - 1)
    return r - v


def lowPosWithMoreThanOneZero(nums):
    p = 0
    while True:
        m = 1 << p
        n = sum(1 if v & m == 0 else 0 for v in nums)
        if n > 1:
            return p
        p += 1


def pairs(n):
    return ((i, j) for i in range(0, n - 1) for j in range(i + 1, n))


def fixPiles(piles):
    highOneP = highOne(xor(piles))
    if highOneP == None:  # the piles are in a winning position
        r = piles
    elif any(zeroAt(v, highOneP) for v in piles):
        r = fixPilesWithZeroAtHigh(piles)
    else:
        r = fixPilesWithoutZeroAtHigh(piles, highOneP)
    return r


def fixPilesWithZeroAtHigh(piles):
    piles = list(piles)
    while True:
        highOneP = highOne(xor(piles))
        if highOneP == None:
            return piles
        candidates = [(i, diffToFlip(v, highOneP)) for i, v in enumerate(piles) if zeroAt(v, highOneP)]
        winner = min(candidates, key=operator.itemgetter(1))
        i, add = winner
        piles[i] += add
    return piles


def fixPilesWithoutZeroAtHigh(piles, highOneP):
    highPiles = [v >> (highOneP + 1) for v in piles]
    highPilesZ = [(v, lowZero(v)) for v in highPiles]
    matches = [(i, j, highOneP + 1 + highPilesZ[i][1]) for i, j in pairs(len(piles)) if
               highPilesZ[i][1] == highPilesZ[j][1]]
    if not matches:
        zeroP = lowPosWithMoreThanOneZero(highPiles)
        lowzs = [i for i, v in enumerate(highPiles) if zeroAt(v, zeroP)]
        nz = len(lowzs)
        baseZeroP = highOneP + 1 + zeroP
        matches = [(lowzs[i], lowzs[j], baseZeroP) for i, j in pairs(nz)]
    results = (fixPilesTwoZeros(piles, zeroP, i, j) for i, j, zeroP in matches)
    return min(results, key=sum)


def fixPilesTwoZeros(piles, zeroP, i, j):
    iAdd = diffToFlip(piles[i], zeroP)
    jAdd = diffToFlip(piles[j], zeroP)
    piles = list(piles)
    piles[i] += iAdd
    piles[j] += jAdd
    return fixPilesWithZeroAtHigh(piles)


def solve(piles):
    fixedPiles = fixPiles(piles)
    return sum(fixedPiles) - sum(piles), fixedPiles


def readLine(): return input()


def readInt(): return int(readLine())


def readInts(): return tuple(int(token) for token in readLine().split())


def readIntList(): return list(readInts())


def main():
    nt = readInt()
    for _ in range(nt):
        _n = readInt()
        piles = readIntList()
        answer, _fixedPiles = solve(piles)
        print(answer)


main()