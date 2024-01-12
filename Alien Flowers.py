m = 1000000007

def inverse_modulo(x):
    return pow(x, m - 2, m)

def count_flower_chains(RR, RB, BB, BR):
    def nCr(n, r):
        n, r = r, n
        n, r = n + r - 1, r - 1
        if r > n:
            return 0
        if r == n:
            return 1
        total = 1
        for x in range(1, r + 1):
            total = (total * (x + n - r) * inverse_modulo(x)) % m
        return total

    total = 0
    if RB == 0 and BR == 0:
        if RR != 0 and BB != 0:
            total = 0
        elif RR == 0 and BB != 0:
            total = 1
        elif BB == 0 and RR != 0:
            total = 1
        else:
            total = 2
    elif RB == BR:
        total = nCr(RB + 1, RR) * nCr(RB, BB)
        total = total % m
        total = total + nCr(RB + 1, BB) * nCr(RB, RR)
        total = total % m
    elif RB == BR + 1:
        total = nCr(RB, RR) * nCr(RB, BB)
        total = total % m
    elif BR == RB + 1:
        total = nCr(BR, RR) * nCr(BR, BB)
        total = total % m
    return total

RR, RB, BB, BR = [int(x) for x in input().strip().split()]
result = count_flower_chains(RR, RB, BB, BR)
print(result)
