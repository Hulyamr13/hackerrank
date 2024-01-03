def mpow(x, n, mod):
    res = 1
    while n:
        if n & 1:
            res = (res * x) % mod
        x = (x * x) % mod
        n //= 2
    return res

def calculate(T, test_cases):
    mod_val = 10**9 + 7
    results = []

    for test in range(1, T + 1):
        n, l, r = test_cases[test - 1]
        m = r - l + 1
        if m == 1:
            results.append(1)
            continue

        v = [1] * (n + 1)
        c = [1] * (n + 1)
        for i in range(1, len(v)):
            v[i] = (v[i - 1] * (m - 2 + i) % mod_val * mpow(i, mod_val - 2, mod_val)) % mod_val
            c[i] = (c[i - 1] * (m - i) % mod_val * mpow(i, mod_val - 2, mod_val)) % mod_val

        sum_val = 0
        for ma in range(1, n + 1):
            zn = 1
            for k in range(1, n // ma + 1):
                if k <= m:
                    sum_val += zn * v[n - k * ma] * m % mod_val * c[k - 1] % mod_val
                    zn *= -1
        sum_val %= mod_val
        if sum_val < 0:
            sum_val += mod_val
        results.append(sum_val)

    return results

if __name__ == "__main__":
    T = int(input())
    test_cases = []
    for _ in range(T):
        n, l, r = map(int, input().split())
        test_cases.append((n, l, r))

    res = calculate(T, test_cases)
    for val in res:
        print(val)
