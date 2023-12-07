#!/bin/python3

import os
import sys
from functools import reduce
from itertools import combinations

cc = 10**9 + 7
d30 = 73741817
D2 = 976371285
D3 = 688423210
D4 = 905611805
D5 = 607723520
D6 = 235042059
D7 = 255718402
D8 = 494499948

def twopower(a):
    if a < 30:
        return (2**a)
    elif a >= 30 and a < 100:
        dvi = a // 30
        rem = a % 30
        ans = ((d30**dvi) % cc) * ((2**rem) % cc)
        ans = ans % cc
        return (ans)
    elif a >= 100 and a <= 1000:
        dvi2 = a // 100
        dvi = a % 100 // 30
        rem = a % 100 % 30
        ans = ((D2**dvi2) % cc) * ((d30**dvi) % cc) * ((2**rem) % cc)
        ans = ans % cc
        return (ans)

def midpower(a):
    if a <= 1000:
        return (twopower(a))
    elif a > 1000 and a <= 10**4:
        x = a // 1000
        y = a % 1000
        z = ((D3**x) % cc) * twopower(y)
        z = z % cc
        return (z)
    elif a > 10**4 and a <= 10**5:
        x1 = a // 10**4
        x2 = a // 10**3 - x1 * 10
        y = a % 10**3
        z = ((D4**x1) % cc) * ((D3**x2) % cc) * twopower(y)
        z = z % cc
        return (z)
    elif a > 10**5 and a <= 10**6:
        x1 = a // 10**5
        x2 = a // 10**4 - x1 * 10
        x3 = a // 10**3 - x2 * 10 - x1 * 100
        y = a % 10**3
        z = ((D5**x1) % cc) * ((D4**x2) % cc) * ((D3**x3) % cc) * twopower(y)
        z = z % cc
        return (z)

def hipower(a):
    if a <= 10**6:
        return (midpower(a))
    elif a > 10**6 and a <= 10**7:
        x = a // 10**6
        y = a % 10**6
        z = ((D6**x) % cc) * midpower(y)
        z = z % cc
        return (z)
    elif a > 10**7 and a <= 10**8:
        x1 = a // 10**7
        x2 = a // 10**6 - x1 * 10
        y = a % 10**6
        z = ((D7**x1) % cc) * ((D6**x2) % cc) * midpower(y)
        z = z % cc
        return (z)
    elif a > 10**8 and a <= 10**9:
        x1 = a // 10**8
        x2 = a // 10**7 - x1 * 10
        x3 = a // 10**6 - x2 * 10 - x1 * 100
        y = a % 10**6
        z = ((D8**x1) % cc) * ((D7**x2) % cc) * ((D6**x3) % cc) * midpower(y)
        z = z % cc
        return (z)

def fanum(a):
    if a % 4 == 0 or a % 4 == 1:
        if (a // 4) % 2 == 0:
            return (int(hipower(a - 2) + hipower(2 * (a // 4) - 1)))
        else:
            return (int(hipower(a - 2) - hipower(2 * (a // 4) - 1)))
    elif a % 4 == 3:
        if (a // 4) % 2 == 0:
            return (int(hipower(a - 2) - hipower(2 * (a // 4))))
        else:
            return (int(hipower(a - 2) + hipower(2 * (a // 4))))
    elif a % 4 == 2:
        return (int(hipower(a - 2)))

def king(army, k):
    lst = []
    for i in army:
        lst.append(fanum(i))
    lst1 = []
    lst1.append(lst)
    for i in range(1, k):
        l = []
        el = 0
        for j in range(i, n):
            el = (el + lst1[i - 1][j - i]) % cc
            l.append((el * lst[j]) % cc)
        lst1.append(l)
    tt = sum(lst1[-1])
    return(tt % cc)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    army = list(map(int, input().rstrip().split()))

    result = king(army, k)

    fptr.write(str(result) + '\n')

    fptr.close()
