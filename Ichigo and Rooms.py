import math

a = [0] * 71112
p = []
for i in range(2, 71112):
    if a[i] == 0:
        for j in range(2, 71112 // i):
            a[i * j] = 1
        p.append(i)

e = 1111

t = int(input())
for _ in range(t):
    n, bb = map(int, input().split())
    if n == 1:
        print(0)
        continue

    k = 2 * n + 1
    b = abs(bb)
    l = math.gcd(b, k)
    k //= l
    m = int(math.sqrt(k))
    l = k
    d = k

    i = 0
    while p[i] <= m:
        if k % p[i] == 0:
            l -= l // p[i]
            while k % p[i] == 0:
                k //= p[i]
        i += 1

    if k > 1:
        l -= l // k

    k = d
    m = int(math.sqrt(l))
    s = l

    for i in range(1, m + 1):
        if l % i == 0:
            j = i
            b = 2
            c = 1
            while j > 0:
                if j % 2 == 1:
                    c = (c * (b // e) % k * e % k + c * (b % e) % k) % k
                b = (b * (b // e) % k * e % k + b * (b % e) % k) % k
                j //= 2
            if c == 1 and s > i:
                s = i

            j = l // i
            b = 2
            c = 1
            while j > 0:
                if j % 2 == 1:
                    c = (c * (b // e) % k * e % k + c * (b % e) % k) % k
                b = (b * (b // e) % k * e % k + b * (b % e) % k) % k
                j //= 2
            if c == 1 and s > l // i:
                s = l // i

    print(2 * n - s)
