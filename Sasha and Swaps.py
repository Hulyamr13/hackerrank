import math

def calculate_cycles_swaps(tfacts, lenstart, p, t):
    cyclelist = {}
    isgood = True
    numswaps = 0
    addablel = -1
    addablecycle = None

    for l in lenstart.keys():
        llen = len(lenstart[l])
        for f in tfacts:
            if f == math.gcd(l * f, t):
                break
        if llen % f != 0:
            isgood = False
        numcycles = llen // f
        addswaps = numcycles * (l * f - 1)

        for i in range(0, llen, f):
            currcycle = [0] * (f * l)
            for j in range(f):
                currpos = lenstart[l][i + j]
                cyclepos = j
                currcycle[cyclepos] = currpos
                for _ in range(1, l):
                    currpos = p[currpos]
                    cyclepos = (cyclepos - t) % (f * l)
                    currcycle[cyclepos] = currpos
            try:
                cyclelist[l].append(currcycle)
            except KeyError:
                cyclelist[l] = [currcycle]

        if numcycles >= 2 and addablel == -1 and 2 * f == math.gcd(2 * l * f, t):
            addablel = l
            addablecycle = [0] * (2 * f * l)
            for j in range(f):
                currpos = lenstart[l][j]
                cyclepos = j
                addablecycle[cyclepos] = currpos
                for _ in range(1, l):
                    currpos = p[currpos]
                    cyclepos = (cyclepos - t) % (2 * f * l)
                    addablecycle[cyclepos] = currpos
            for j in range(f):
                currpos = lenstart[l][f + j]
                cyclepos = j + f
                addablecycle[cyclepos] = currpos
                for _ in range(1, l):
                    currpos = p[currpos]
                    cyclepos = (cyclepos - t) % (2 * f * l)
                    addablecycle[cyclepos] = currpos
        numswaps += addswaps

    return cyclelist, addablel, addablecycle, isgood, numswaps

def find_addable_cycle(l, f, lenstart, p, t):
    addablecycle = [0] * (2 * f * l)

    for j in range(f):
        currpos = lenstart[l][j]
        cyclepos = j
        addablecycle[cyclepos] = currpos
        for _ in range(1, l):
            currpos = p[currpos]
            cyclepos = (cyclepos - t) % (2 * f * l)
            addablecycle[cyclepos] = currpos

    for j in range(f):
        currpos = lenstart[l][f + j]
        cyclepos = j + f
        addablecycle[cyclepos] = currpos
        for _ in range(1, l):
            currpos = p[currpos]
            cyclepos = (cyclepos - t) % (2 * f * l)
            addablecycle[cyclepos] = currpos

    return addablecycle

def main():
    [n, k, t] = list(map(int, input().split()))
    p = list(map(lambda x: int(x) - 1, input().split()))
    lens = [0] * n
    lenstart = dict()

    for i in range(n):
        if lens[i] == 0:
            curr = p[i]
            steps = 1
            while curr != i:
                curr = p[curr]
                steps += 1
            lens[i] = steps
            curr = p[i]
            while curr != i:
                lens[curr] = steps
                curr = p[curr]
            try:
                lenstart[steps].append(i)
            except KeyError:
                lenstart[steps] = [i]

    tfacts = set()

    for i in range(1, 1 + int(math.sqrt(t))):
        if t % i == 0:
            tfacts.add(i)
            tfacts.add(t // i)

    tfacts = sorted(list(tfacts))

    cyclelist, addablel, addablecycle, isgood, numswaps = calculate_cycles_swaps(tfacts, lenstart, p, t)

    if isgood and numswaps <= k:
        if (k - numswaps) % 2 == 0 or addablel != -1:
            if (k - numswaps) % 2 == 1:
                cyclelist[addablel] = cyclelist[addablel][2:]
                numswaps += 1
                cyclelist[0] = [addablecycle]

            for l in cyclelist.keys():
                for cycle in cyclelist[l]:
                    initpos = cycle[0]
                    for x in cycle[1:]:
                        print(initpos + 1, x + 1)

            for _ in range(k - numswaps):
                print("1 2")
        else:
            print("no solution")
    else:
        print("no solution")

if __name__ == "__main__":
    main()
