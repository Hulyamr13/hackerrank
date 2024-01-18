# Enter your code here. Read input from STDIN. Print output to STDOUT

from os.path import isfile
from os import getcwd
from sys import stdin, modules
import re

lolPath = getcwd()
randid = "\qosdjfoiz.txt"
home = isfile(lolPath + randid)

modo = 10 ** 9 + 7


def inv(n):
    return pow(n, modo - 2, modo)


def shrt(strn):
    return strn if len(strn) < 80 else strn[:38] + (
        '....' if type(strn).__name__ == 'str' else [None, None, None]) + strn[-38:]


def doRep9(n):
    return (pow(5, n + 1, modo) - 1) * inv(4) % modo


def modFull(strx, N=1):
    ln, nd = len(strx), 100
    q, r = divmod(ln, nd)
    rs = int(strx[:r]) if r else 0
    for ix in range(r, ln, nd):
        rs = (rs * 10 ** nd + int(strx[ix:ix + nd])) % modo
    po10 = pow(10, ln, modo)
    rs = (rs * (pow(po10, N, modo) - 1) * (inv(po10 - 1))) % modo
    return rs


def fairePrefixe(pref, n):
    fd = [0, 1, 2, 3, 4, 4, 4, 4, 4, 6]
    val = (pow(5, n + 1, modo) - 1) * inv(4)
    rs = 0
    for d in reversed(pref):
        rs += int(d) * val
        val = (5 * val + 1) % modo
    rs = (rs + doRep9(n)) % modo
    return rs


def doUn(strx):
    fd = [0, 1, 2, 3, 4, 4, 4, 4, 4, 6]
    val = 6
    res = 1
    for ds in reversed(strx[:-1]):
        res = (res + int(ds) * val) % modo
        val = (val * 5 + 1) % modo
    res += fd[int(strx[-1])]
    return res % modo


def doMult(lx, N):
    r1 = doUn(lx)
    pom = len(lx)
    sud = sum(int(x) for x in lx)
    pi, n = pow(5, pom) % modo, N - 1
    invpi = inv(pi - 1)
    spo = (pow(pi, N, modo) - 1) * invpi
    srep = (pi * (pow(pi, n, modo) - 1) * invpi - n) * inv(4) % modo
    res = (spo * (r1 - 1) + sud * srep) % modo
    return res


def faire2(lx, N):
    full = modFull(lx, N)
    m = re.search('[^01234]', lx)
    if not m:
        return (full - doMult(lx, N)) % modo

    m = re.search('[^01234]', lx)
    pos = m.span(0)[0]
    dl = 1 if (N == 1 or pos == 0) and m.group(0) == '9' and not re.search('[^9]', lx[pos:]) else 0
    n, prfx = len(lx) * N - pos, lx[:pos]
    rs = fairePrefixe(prfx, n) - 2 + dl
    return (full - rs) % modo


if modules[__name__].__name__ == '__main__':
    if home:
        prv = 0
        print("lecture ")
        lif = [open(lolPath + '\IrresponsibleNumbersIn' + filn + '.txt') for filn in ('07', '20', '13', '14', '15')]
    else:
        trace = 0
        lif = [stdin]

    for rd in lif:
        try:
            if home:
                print(rd.name)
            while True:
                x, strn = rd.readline().strip().split()
                n = int(strn)
                if home:
                    print(shrt(x), n)
                    lif = faire2,
                    prv = None
                else:
                    lif = [faire2]
                for f in lif:
                    if home:
                        cr = ch()
                    r = f(x, n)
                    if home:
                        t = cr.lap()
                        print("\t", f.__name__, r, t, prv == r if prv else '', prv if prv and prv != r else '')
                        prv = r
                    else:
                        print(r)
        except EOFError:
            pass
        except ValueError:
            pass
