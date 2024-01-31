# Enter your code here. Read input from STDIN. Print output to STDOUT

sieve = [True] * (10**3 + 1)

for i in range(0, 10**3 + 1, 2):
    sieve[i] = False

for j in range(3, int(10**3) + 1, 2):
    if sieve[j]:
        for k in range(j * 2, 10**3 + 1, j):
            sieve[k] = False

sieve[1], sieve[2] = False, True

def totient(n):
    m = 1
    ans = 0
    for i in range(2, 1000):
        if sieve[i]:
            if m * i >= n:
                return m
            else:
                m = m * i
                ans += i // (i - 1)

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(totient(n))
