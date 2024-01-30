# Enter your code here. Read input from STDIN. Print output to STDOUT

import random

def miller_rabin(n, k=5):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

n = int(input())
pct = 61
cntp = 0
k = 1
while n <= pct:
    d4 = (2 * k + 1) ** 2
    cntp += len(list(filter(miller_rabin, [d4 - 2 * j * k for j in range(1, 4)])))
    pct = 100 * cntp / (1 + 4 * k)
    k += 1
print(2 * k - 1)
