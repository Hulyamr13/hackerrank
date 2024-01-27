# Enter your code here. Read input from STDIN. Print output to STDOUT

mod = 10 ** 9 + 7

ext_gcd = lambda a, b: (1, 0, a) if b == 0 else (lambda x, y, g: (y, x - (a // b) * y, g))( *ext_gcd(b, a % b))

mod_inv = lambda a: (lambda x, y, g: (x % mod + mod) % mod)(*ext_gcd(a, mod))

def main():
    pot = [0] * 1100000
    ch = [[0] * 1100 for _ in range(1100)]
    s = [0] * 1100
    nn = [0] * 1100

    pot[0] = 1
    for i in range(1, 1100000):
        pot[i] = (pot[i - 1] * 2) % mod

    for i in range(1001):
        for j in range(i + 1):
            ch[i][j] = 1 if j == 0 else (ch[i - 1][j - 1] + ch[i - 1][j]) % mod

    nn[0] = 1
    for n in range(1, 1001):
        for i in range(1, n + 1):
            th = (ch[n][i] * pot[i * (n - 1)]) % mod
            nn[n] -= th * nn[n - i]
            nn[n] = ((nn[n] % mod) + mod) % mod

        nnn = nn[n]
        for i in range(1, n):
            th = (ch[n - 1][i - 1] * s[i]) % mod
            th = (th * nn[n - i]) % mod
            nnn = (nnn + th) % mod

        s[n] = mod - nnn

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(s[n])

if __name__ == "__main__":
    main()
