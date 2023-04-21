numsets = int(input())


def findMaxMoves(ele, sum):
    sum = sum / 2
    if sum == 0:
        if ele != [0 for x in range(0, len(ele))]:
            return 0
        else:
            return len(ele) - 1
    s = 0
    i = 0
    n = len(ele)
    if len(ele) == 1 or len(ele) == 0:
        return 0
    while s != sum and i < n:
        s += ele[i]
        i += 1
    if i >= n:
        return 0
    return 1 + max(findMaxMoves(ele[0:i], sum), findMaxMoves(ele[i:n], sum))


def findMaxDeepness(array, amin, amax):
    if ((amin + amax) % 2 == 0 and (amin + amax) / 2 in array):
        return 1 + max(findMaxDeepness(array, amin, (amin + amax) / 2), findMaxDeepness(array, (amin + amax) / 2, amax))
    return 0


for i in range(numsets):
    els = int(input())
    values = [int(x) for x in input().split(' ')]

    print(findMaxMoves(values, sum(values)))

