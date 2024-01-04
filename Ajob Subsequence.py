# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 1000 * 1000 * 1000 + 7

def power(a, n, p):
    res = 1
    while n:
        if n & 1:
            res = (res * a) % p
        a = (a * a) % p
        n //= 2
    return res

def c(n, k, p):
    res = 1
    f = [0] * p
    inv = [0] * p
    f[0] = inv[0] = 1
    for i in range(1, p):
        f[i] = (f[i - 1] * i) % p
    while n > 0 or k > 0:
        n1 = n % p
        n //= p
        k1 = k % p
        k //= p
        if n1 < k1:
            return 0
        res = (res * ((f[n1] * power(f[k1], p - 2, p) * power(f[n1 - k1], p - 2, p)) % p)) % p
    return res


t = int(input())
for _ in range(t):
    n, k, p = map(int, input().split())
    print(c(n + 1, k + 1, p))
