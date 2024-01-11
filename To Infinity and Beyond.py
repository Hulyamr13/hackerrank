MOD = 1000000007

def power_mod(a, k, m):
    if k == 0:
        return 1
    res = power_mod(a, k // 2, m)
    if k % 2 == 0:
        return (res * res) % m
    return (a * res * res) % m

t = int(input())

facs = [0] * 1000010
invfacs = [0] * 1000010
invs = [0] * 1000010

facs[0] = 1
for i in range(1, 1000010):
    facs[i] = (facs[i - 1] * i) % MOD

invfacs[1000009] = power_mod(facs[1000009], MOD - 2, MOD)
for i in range(1000008, -1, -1):
    invfacs[i] = (invfacs[i + 1] * (i + 1)) % MOD

for i in range(1, 1000010):
    invs[i] = (invfacs[i] * facs[i - 1]) % MOD

for _ in range(t):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    if a > b:
        a, b = b, a
    s = 0
    b1 = (b + 1) % MOD
    b2 = (a + 1) % MOD
    for r in range(a + 1):
        s = (s + b1 * b2) % MOD
        r2inv = invs[r + 2]
        b1 = (b - r) % MOD * r2inv % MOD * b1 % MOD
        b2 = (a - r) % MOD * r2inv % MOD * b2 % MOD
    b3 = 1
    b1 = (b + 1) % MOD
    b2 = (a + 1) % MOD
    res = 0
    for l in range(min(a, c) + 1):
        res = (res + s * b3) % MOD
        s = (s + MOD - b1 * b2 % MOD) % MOD
        r2inv = invs[l + 2]
        b1 = (b - l) % MOD * r2inv % MOD * b1 % MOD
        b2 = (a - l) % MOD * r2inv % MOD * b2 % MOD
        b3 = (c - l) % MOD * invs[l + 1] % MOD * b3 % MOD
    print(res)
