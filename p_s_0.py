import sys

def get_num_final(N, P):
    ls = int(P ** 0.5) + 1
    cn = [i for i in range(ls)]
    ca = [P // i for i in range(1, ls)]
    ca.insert(0, 0)
    gs = [(P // (i - 1) - P // i) for i in range(2, ls)]
    gs.insert(0, 0)
    gs.append(ca[-1] - cn[-1])
    pn = list(cn)
    pa = list(ca)
    for n in range(N - 1):
        for i in range(1, ls):
            cn[i] = (pa[i] + cn[i - 1]) % (10 ** 9 + 7)
        ca[-1] = (cn[-1] + (pn[-1]) * (gs[-1])) % (10 ** 9 + 7)
        for i in range(ls - 2, 0, -1):
            ca[i] = ((pn[i]) * (gs[i]) + ca[i + 1]) % (10 ** 9 + 7)
        pn = list(cn)
        pa = list(ca)

    print(ca[1] % (10 ** 9 + 7))


N = int(input())
P = int(input())

get_num_final(N, P)