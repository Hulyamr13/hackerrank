# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 10**9 + 7

def calc_oneline(m):
    ret = [6]
    c = [1] * 6
    for _ in range(m + 1):
        c = [c[5], c[3] * 3 % MOD, c[0] * 3 % MOD, c[4], c[1] * 3 % MOD, c[2]]
        ret.append(sum(c) % MOD)
    return ret

oneline = calc_oneline(1024)

def ppow(a, b):
    return pow(a, b, MOD)

def solve(m, n):
    c1 = 27
    c2 = (ppow(2, n // 3) + ppow(2, (n + 1) // 3) + ppow(2, (n + 2) // 3) - 6) % MOD * 9
    c3 = 9
    c4 = (ppow(3, n // 3) + ppow(3, (n + 1) // 3) + ppow(3, (n + 2) // 3) - ppow(2, n // 3) - ppow(2, (n + 1) // 3) - ppow(2, (n + 2) // 3) - 3) % MOD * 6
    c5 = (oneline[n] - c1 - c2 - c3 - c4) % MOD

    r = ppow(3, 2 * m // 3) + ppow(3, (2 * m + 1) // 3) + ppow(3, (2 * m + 2) // 3)
    r += (ppow(2, n // 3) + ppow(2, (n + 1) // 3) + ppow(2, (n + 2) // 3) - 6) % MOD * (ppow(3, m // 3) + ppow(3, (m + 1) // 3) + ppow(3, (m + 2) // 3)) % MOD
    r += ppow(3, m // 3) + ppow(3, (m + 1) // 3) + ppow(3, (m + 2) // 3)
    r += (ppow(3, n // 3) + ppow(3, (n + 1) // 3) + ppow(3, (n + 2) // 3) - ppow(2, n // 3) - ppow(2, (n + 1) // 3) - ppow(2, (n + 2) // 3) - 3) % MOD * (ppow(2, m // 3) + ppow(2, (m + 1) // 3) + ppow(2, (m + 2) // 3)) % MOD
    r += c5
    return r % MOD

c = int(input())
for _ in range(c):
    m, n = map(int, input().split())
    print(solve(m, n))
