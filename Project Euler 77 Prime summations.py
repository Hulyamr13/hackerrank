# Enter your code here. Read input from STDIN. Print output to STDOUT

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n + 1) if primes[i]]


def prime_partitions(n):
    primes = sieve_of_eratosthenes(n)
    dp = [0] * (n + 1)
    dp[0] = 1
    for p in primes:
        for i in range(p, n + 1):
            dp[i] += dp[i - p]
    return dp[n]


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(prime_partitions(n))
