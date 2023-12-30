# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 10**9 + 7

def mul_m(a, b):
    return (a * b) % MOD

def zpow(a, b):
    return 0 if b == 0 else pow(a, b, MOD)

if __name__ == "__main__":
    n = int(input())
    p, b, a = [], [], []

    for _ in range(n):
        pi, bi, ai = map(int, input().split())
        p.append(pi)
        b.append(bi)
        a.append(ai)

    B = 1
    for i in range(n):
        B = mul_m(B, zpow(p[i], b[i]))

    if all(a[i] == b[i] for i in range(n)):
        print((B * 2) % MOD)
    else:
        C = 1
        for i in range(n):
            C = mul_m(C, 1 + zpow(p[i], a[i] - b[i]))
        print((B * C) % MOD)
