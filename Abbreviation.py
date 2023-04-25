def check_possibility(a, b):
    bpos = {}
    for i in range(len(b)):
        bpos[b[i]] = (bpos[b[i]] | set([i])) if b[i] in bpos else set([i])
    possibilities = set([0])
    for i in range(len(a)):
        if a[i].upper() in bpos:
            intersection = bpos[a[i].upper()] & possibilities
            advancement = set([i + 1 for i in intersection])
        else:
            advancement = set([])
        if a[i].upper() == a[i]:
            possibilities = advancement
        else:
            possibilities = possibilities | advancement
    return "YES" if (len(b)) in possibilities else "NO"


if __name__ == '__main__':
    q = int(input().strip())
    for i in range(q):
        a = input().strip()
        b = input().strip()
        result = check_possibility(a, b)
        print(result)
