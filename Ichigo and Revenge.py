# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 10**9 + 7

def mod_exp(a, b, n):
    c = 1
    d = a
    while b:
        if b & 1:
            c = (c * d) % n
        d = (d * d) % n
        b >>= 1
    return c

def inv(num):
    return mod_exp(num, MOD - 2, MOD)

def init():
    fact = [0] * 100001
    fact[0] = 1
    for i in range(1, 100001):
        fact[i] = (fact[i - 1] * i) % MOD
    return fact

def c(n, m, fact):
    tmp = (fact[n] * inv(fact[m])) % MOD
    return (tmp * inv(fact[n - m])) % MOD


fact = init()
t = int(input())
for _ in range(t):
    u, v, k, p = map(int, input().split())
    val1 = c(u * p, v * p, fact)
    val2 = c(u, v, fact)
    val3 = inv(p)
    val4 = (val1 + MOD - val2) % MOD
    val = (val4 * val3) % MOD
    if k == 0:
        val = (val + c(u, v, fact)) % MOD
    print(val)
