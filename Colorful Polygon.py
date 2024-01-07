# Enter your code here. Read input from STDIN. Print output to STDOUT

mod = 10**9 + 7

def add(x, y):
    x += y
    x %= mod
    return x

def upd(d, i, di):
    while i < len(d):
        d[i] = add(d[i], di)
        i |= i + 1

def sum(d, r):
    ans = 0
    while r >= 0:
        ans = add(ans, d[r])
        r = (r & (r + 1)) - 1
    return ans

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [x - 1 for x in a]

    maxdif = n + 1
    starti = 0
    used = [0] * n
    j = 0
    for i in range(n):
        while j < n and not used[a[j]]:
            used[a[j]] = 1
            j += 1
        if j != n and j - i < maxdif:
            maxdif = j - i
            starti = i
        used[a[i]] = 0

    a = a[starti:] + a[:starti]

    rg = [0] * n
    used = [0] * n
    j = 0
    for i in range(n):
        while j < n and not used[a[j]]:
            used[a[j]] = 1
            j += 1
        rg[i] = j
        used[a[i]] = 0

    ans = 0
    d = [0] * n
    usedPfx = [0] * n
    usedSfx = [0] * n
    for fsPick in range(n):
        d = [0] * n
        upd(d, fsPick, 1)
        upd(d, fsPick + 1, -1)

        for i in range(fsPick, n - 1):
            cur = sum(d, i)
            ni = min(rg[i + 1], n - 1)
            upd(d, i + 1, cur)
            upd(d, ni + 1, -cur)

        usedSfx = usedPfx[:]
        lastPick = n - 1
        while lastPick > fsPick:
            ans = add(ans, sum(d, lastPick))
            if usedSfx[a[lastPick]]:
                break
            usedSfx[a[lastPick]] = 1
            lastPick -= 1

        if usedPfx[a[fsPick]]:
            break
        usedPfx[a[fsPick]] = 1

    print(ans)

if __name__ == "__main__":
    main()
