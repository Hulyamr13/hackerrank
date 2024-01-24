def formposicaodig(x):
    n = len(str(x))
    return 1 + (x - 10**(n-1)) * n + n * 10**(n-1) + (1 - 10**n) // 9

def formInvposicaodig(pos):
    n = len(str(pos))
    xcalc = (pos + (10**n - 1) // 9 - 1) // n
    while n != len(str(xcalc)):
        n = len(str(xcalc))
        xcalc = (pos + (10**n - 1) // 9 - 1) // n
    return int(str(xcalc)[pos - formposicaodig(xcalc)])

n = int(input())
for k in range(n):
    prd = 1
    for j in map(int, input().split()):
        nth = formInvposicaodig(j)
        if nth == 0:
            prd = 0
            break
        else:
            prd *= nth
    print(prd)
