def change_coins(amount, coins):
    ways = 0
    for coin in coins:
        if amount == coin:
            return ways + 1
        if amount < coin:
            return ways
        ways += change_coins(amount - coin, coins)
    return ways

def multiply_modulo(T, te, n):
    result = [0 for _ in range(15)]
    for i in range(15):
        for j in range(15):
            result[i] += T[i][j] * te[j]
            result[i] %= MOD
    return result

def multiply_two_modulo(T1, T2):
    result = [[0 for _ in range(15)] for _ in range(15)]
    for i in range(15):
        for j in range(15):
            for k in range(15):
                result[i][j] += T1[i][k] * T2[k][j]
                result[i][j] %= MOD
    return result

def mod_exponentiation(T, e):
    result = [[0 for _ in range(15)] for _ in range(15)]
    for i in range(15):
        result[i][i] = 1
    while e:
        if e & 1:
            result = multiply_two_modulo(result, T)
        T = multiply_two_modulo(T, T)
        e //= 2
    return result

n = int(input())
k = int(input())
MOD = 10**9 + 7
pre = 15
a = list(map(int, input().split()))
a = sorted(a)
init_ans = [0 for _ in range(pre + 1)]
te = [0 for _ in range(pre)]
b = 0
for i in range(1, pre + 1):
    init_ans[i] = change_coins(i, a) % MOD
    te[i - 1] = init_ans[i]

if n <= pre:
    print((change_coins(n, a) * 2) % MOD)
else:
    T = [[0 for _ in range(15)] for _ in range(15)]
    for i in range(k):
        T[14][15 - a[i]] = 1
    for i in range(14):
        T[i][i + 1] = 1
    p1 = n // 15
    T = mod_exponentiation(T, 15 * p1)
    print((multiply_modulo(T, te, n)[n - 15 * p1 - 1] * 2) % MOD)
