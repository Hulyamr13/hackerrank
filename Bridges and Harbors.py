import math
from typing import List

Dp = []


def main():
    t = int(input())
    for _ in range(t):
        n, m, k, mod = map(int, input().split())
        print(solve(n, m, k, mod))


def init(n: int, m: int, k: int, p: int):
    global Dp
    max_val = m * k
    c_matrix = [[0] * (k + 1) for _ in range(max_val + 1)]

    for i in range(max_val + 1):
        c_matrix[i][0] = 1

    for i in range(k + 1):
        c_matrix[i][i] = 1

    for i in range(2, max_val + 1):
        for j in range(1, (i // 2) + 1 if i // 2 <= k else k + 1):
            c_matrix[i][j] = (c_matrix[i - 1][j - 1] + c_matrix[i - 1][j]) % p
            if i - j <= k:
                c_matrix[i][i - j] = c_matrix[i][j]

    Dp = [[0] * (m + 1) for _ in range(max_val + 1)]

    for i in range(m + 1):
        Dp[0][i] = 1

    for i in range(1, max_val + 1):
        for j in range(1, m + 1):
            result = Dp[i - 1][j]
            result -= c_matrix[i - 1][k] * Dp[i - k - 1][j - 1] % p if i > k else 0
            Dp[i][j] = (result * j % p + p) % p


def solve(n: int, m: int, k: int, mod: int) -> int:
    init(n, m, k, mod)
    result = 0
    max_val = m * k
    out_edge = n - m

    if out_edge == 0:
        return 1 % mod

    end = min(max_val, out_edge)
    cmn_values = cmn(n - m - 1, max_val, mod)
    power = power_mod(n - m, out_edge - end, mod)

    for d in range(end, 0, -1):
        mul = cmn_values[d - 1]
        result += Dp[d][m] * power % mod * mul % mod
        power = power * (n - m) % mod
        if power == 0:
            break

    cmn_values = cmn(n, m, mod)
    result = result % mod * cmn_values[m] % mod
    return result


def cmn(m: int, n: int, mod: int) -> List[int]:
    n = min(m, n)
    factors = get_factors(mod)
    powers = [0] * len(factors)
    c_powers = [0] * len(factors)
    ups = [0] * len(factors)

    for i in range(len(factors)):
        p = factors[i]
        power = 1
        while mod % p == 0:
            mod //= p
            power *= p
        powers[i] = power
        ups[i] = c_powers[i] = 1

    result = [0] * (n + 1)
    result[0] = 1

    for i in range(n):
        lcm = 1
        c_result = 0

        for j in range(len(factors)):
            p = factors[j]
            power = powers[j]
            mul_up = m - i
            mul_down = i + 1

            while mul_up % p == 0:
                mul_up //= p
                c_powers[j] *= p

            while mul_down % p == 0:
                mul_down //= p
                c_powers[j] //= p

            ups[j] = ups[j] * mul_up % power * inv_mod(mul_down, power) % power
            c_result = crt(power, ups[j] * c_powers[j] % power, lcm, c_result)
            lcm *= power

        result[i + 1] = c_result

    return result


def crt(p1: int, m1: int, p2: int, m2: int) -> int:
    result = m2 - m1
    inv = inv_mod(p1, p2)
    result = result * inv % p2
    result = result * p1 + m1

    if result < 0:
        result += p1 * p2

    return result


def get_factors(n: int) -> List[int]:
    result = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if i * i > n:
            break
        if n % i == 0:
            result.append(i)
            while n % i == 0:
                n //= i

    if n != 1:
        result.append(n)
    return result


def power_mod(a: int, power: int, n: int) -> int:
    mod = 1
    a %= n

    while power != 0:
        if power & 1 == 1:
            mod = mod * a % n
        a = a * a % n
        power >>= 1

    return mod


def inv_mod(e: int, f: int) -> int:
    x2, x3 = 0, f
    y2, y3 = 1, e

    while True:
        if y3 == 0:
            return 0
        if y3 == 1:
            if y2 < 0:
                y2 += f
            return y2

        q = x3 // y3
        t2 = x2 - q * y2
        t3 = x3 - q * y3
        x2, x3 = y2, y3
        y2, y3 = t2, t3


if __name__ == "__main__":
    main()
