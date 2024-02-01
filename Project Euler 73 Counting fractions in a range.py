# maximum denominator
maxD = 12000

# algorithm I:
# count mediants between 1/fromD and 1/toD using recursion
def recursion(fromD, toD):
    mediantD = fromD + toD
    # denominator too big ?
    if mediantD > maxD:
        return 0

    # recursion
    return 1 + recursion(fromD, mediantD) + recursion(mediantD, toD)

# algorithm II:
# iteratively enumerate all denominators
def iteration(fromD, toD):
    # find denominator of closest mediant of "from"
    # initial mediant
    d = fromD + toD
    # is there a mediant closer to fromD ?
    while d + fromD <= maxD:
        d += fromD

    # if prevD and d are denominators of adjacent fractions prevN/prevD and n/d
    # then the next denominator is nextD = maxD - (maxD + prevD) % d
    prevD = fromD

    count = 0
    # until we reach the final denominator
    while d != toD:
        # find next denominator
        nextD = maxD - (maxD + prevD) % d

        # shift denominators, the current becomes the previous
        prevD = d
        d = nextD

        count += 1

    return count

# algorithm III:
# return numbers of irreducible fractions a/b < n/d where b is less than maxD
def rank(n, d):
    # algorithm from "Computer Order Statistics in the Farey Sequence" by C. & M. Patrascu
    data = [i * n // d for i in range(maxD + 1)]

    # remove all multiples of 2*i, 3*i, 4*i, ...
    # similar to a prime sieve
    for i in range(1, maxD + 1):
        for j in range(2*i, maxD + 1, i):
            data[j] -= data[i]

    # return sum of all elements
    return sum(data)

# denominators are abbreviated D
toD = 2  # which means 1/2 (original problem)

# Input
toD, maxD = map(int, input().split())

# the algorithm searches from 1/fromD to 1/toD
fromD = toD + 1

# algorithm 3
result = rank(1, toD) - rank(1, fromD) - 1
print(result)

