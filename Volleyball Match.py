# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 1000000007

def calculate_combinations(n, k):
    ret = 1
    for i in range(k):
        ret = ret * (n - i) // (i + 1)
    return ret % MOD


def count_sequences(x, y):
    if y < 25:
        return 0
    if y == 25:
        return 0 if x >= 24 else calculate_combinations(24 + x, x)
    return 0 if y - x != 2 else calculate_combinations(48, 24) * pow(2, y - 26, MOD) % MOD


a, b = sorted(map(int, [input(), input()]))
print(count_sequences(a, b))

