MOD = 10 ** 9 + 7


def lcm(lst):
    ans = 1
    for x in lst:
        ans = ans * x // gcd(ans, x)
    return ans


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a


def getsoltable(a, m, MOD=MOD):
    soltable = [1] + [0] * (len(a) * m - 1)
    for x in a:
        oldsoltable = soltable
        soltable = list(soltable)
        for i in range(x, len(soltable)):
            soltable[i] = (oldsoltable[i] + soltable[i - x]) % MOD
    return soltable


def countsols(const, soltable, lcm):
    offset = const % lcm
    pts = soltable[offset::lcm]
    assert len(pts) == len(a)
    coef = polycoef(pts)
    return polyval(coef, const // lcm)


def polycoef(pts):
    coef = []
    for x, y in enumerate(pts):
        fact = descpower = 1
        for i, c in enumerate(coef):
            y -= descpower * c // fact
            descpower *= x - i
            fact *= i + 1
        coef.append(y)
    return coef


def polyval(coef, x):
    ans = 0
    fact = descpower = 1
    for i, c in enumerate(coef):
        ans += c * descpower * pow(fact, MOD - 2, MOD)
        descpower = descpower * (x - i) % MOD
        fact *= i + 1
    return ans % MOD


n = int(input())
a = [1] + [int(fld) for fld in input().strip().split()]
L, R = [int(fld) for fld in input().strip().split()]
m = lcm(a)
soltable = getsoltable(a, m)
print((countsols(R, soltable, m) - countsols(L - 1, soltable, m)) % MOD)