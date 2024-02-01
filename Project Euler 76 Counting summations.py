# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 10**9 + 7

def get_ways(n):
    res = [0] * (n + 1)
    res[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            res[j] += res[j - i] % MOD
    return res[n] % MOD

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(get_ways(n))
