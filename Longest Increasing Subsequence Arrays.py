mod = 10**9 + 7

def solve1(m, n):
    a = [1] + [0] * n

    for i in range(m):
        b = [0] * (n + 1)
        for j in range(n):
            b[j] += (n - 1) * a[j]
            b[j + 1] += a[j]
        b[-1] += n * a[-1]
        a = list(map(lambda x: x % mod, b))

    return a[-1]


def ex_gcd(b, s):
    w, x, y, z = 1, 0, 0, 1
    while s != 0:
        q = b // s
        b, s, w, x, y, z = s, b % s, y, z, w - q * y, x - q * z
    return (b, w, x)


def modinv(a, p):
    return ex_gcd(p, a)[2] % p


memomodinv = [0]
for i in range(1, 10**5 + 1):
    memomodinv.append(modinv(i, mod))


def solve2(m, n):
    bin_co = 1
    top, bot = m, 1
    val = 0
    power = pow(n - 1, m, mod)
    x_inv = modinv(n - 1, mod)
    for i in range(n):
        val += bin_co * power
        power *= x_inv
        power %= mod
        bin_co *= top
        bin_co *= memomodinv[bot]
        bin_co %= mod
        top -= 1
        bot += 1
    sol = pow(n, m, mod) - val
    return sol % mod


num_test_cases = int(input())

for _ in range(num_test_cases):
    m, n = map(int, input().split())
    print(solve2(m, n))
