def is_prime(x):
    if x in (0, 1):
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

prime = list(map(is_prime, range(0,2000)))

cache = {}
digits = range(0, 10)

def rec_scan(key):
    (x, a, b) = key

    if x == 1:
        count = 0
        for d in digits:
            if prime[a + d] and prime[b + d*d]:
                count += 1
    else:
        count = 0
        for d in digits:
            subkey = (x - 1, a + d, b + d*d)
            if subkey in cache:
                count += cache[subkey]
            else:
                count += rec_scan(subkey)

    cache[key] = count
    return count

def full_scan(x, a, b):
    key = (x, a, b)
    if key in cache:
        return cache[key]
    return rec_scan(key)

def partial_scan(x, q):
    m = q % 10
    q //= 10
    a = 0
    b = 0
    while q > 0:
        t = q % 10
        a += t
        b += t*t
        q //= 10
    if x == 1:
        count = 0
        for d in range(0, m):
            if prime[a + d] and prime[b + d*d]:
                count += 1
    else:
        count = 0
        for d in range(0, m):
            count += full_scan(x - 1, a + d, b + d*d)
    return count

top_cache = {}

def solve(x):
    key = x
    if key in top_cache:
        return top_cache[key]
    x += 1
    if x in top_cache:
        return top_cache[x]
    level = 1
    result = 0
    while x > 0:
        result += partial_scan(level, x)
        level += 1
        x //= 10
    top_cache[key] = result
    return result

def calculate(low, high):
    return solve(high) - solve(low - 1)

count = int(input())

while count > 0:
    count -= 1
    (low, high) = [int(i) for i in input().split() if i != '']
    print(calculate(low, high))