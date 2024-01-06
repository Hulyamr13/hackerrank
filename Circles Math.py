# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 10 ** 9 + 7
f_cache = {0: 1, 1: 1, 'max_key': 1}


def fast_pow_mod(x, pow, MOD):
    if pow == 0:
        return 1
    if pow % 2 == 1:
        return x * fast_pow_mod(x, pow - 1, MOD) % MOD
    else:
        y = fast_pow_mod(x, pow // 2, MOD)
        return y * y % MOD


def modular_inverse(x):
    return fast_pow_mod(x, MOD - 2, MOD)


def fact_mod(n):
    global f_cache
    if n not in f_cache:
        for x in range(f_cache['max_key'] + 1, n + 1):
            f_cache[x] = f_cache[x - 1] * x % MOD
        f_cache['max_key'] = max(f_cache['max_key'], n)

    return f_cache[n]


D = [1, 0]
for x in range(2, 10 ** 6 + 1):
    D.append((x * D[x - 1] + (-1) ** x) % MOD)

T = int(input().strip())

for _ in range(T):
    n, k = map(int, input().strip().split())

    if k == 1:
        print(0)
    else:

        result = 0
        for q in range(1, n // k + 1):
            result = (result + fact_mod(n) * modular_inverse((fact_mod(k) ** q) * fact_mod(n - q * k)) * \
                      (fact_mod(k - 1) ** q) * (-1) ** (q + 1) * \
                      modular_inverse(fact_mod(q)) * D[n - q * k]) % MOD

        print(result % MOD)
