# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

MOD = 1000003
cache = {}
fact, inv_fact = [1] + (MOD - 1) * [0], [1] + (MOD - 1) * [0]

for k in range(1, MOD):
    fact[k] = fact[k - 1] * k % MOD

inv_fact[MOD - 1] = pow(fact[MOD - 1], MOD - 2, MOD)

for k in range(MOD - 1, 1, -1):
    inv_fact[k - 1] = inv_fact[k] * k % MOD

def calculate_combination(n, k, MOD):
    if k < 0: return 0
    if k > n: return 0
    if k == 0 or k == n: return 1
    if n < MOD: return (fact[n] * inv_fact[k] * inv_fact[n - k]) % MOD
    else: return (calculate_combination(n // MOD, k // MOD, MOD) * calculate_combination(n % MOD, k % MOD, MOD)) % MOD

def calculate_rec(n, k, C, letter, used):
    key = (letter, used)
    if letter > 'Z': return 1
    if key in cache: return cache[key]
    ans = calculate_rec(n, k, C, chr(ord(letter) + 1), used)
    for i in range(1, C[letter] + 1):
        ans += (calculate_combination(n - used - k * (i - 1), i, MOD) * calculate_rec(n, k, C, chr(ord(letter) + 1), used + i)) % MOD
    cache[key] = ans % MOD
    return cache[key]

def calculate_possibilities():
    n, k = map(int, input().split())
    print(calculate_rec(n, k, Counter(input()), 'A', 0))

calculate_possibilities()
