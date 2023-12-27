mod = 1000000007


def powmod(b, e):
    if e == 0:
        return 1
    c = powmod(b, e // 2)
    d = (c * c) % mod
    if e % 2:
        return (b * d) % mod
    else:
        return d


def rational_sums(n, a, b):
    c = []
    for i in range(n):
        p = 0
        q = 1
        for j in range(n):
            if i != j:
                q = (q * (mod - a[i] + a[j])) % mod
        for j in range(n - 1):
            p = (p * (mod - a[i])) % mod
            p = (p + b[n - 2 - j]) % mod
        c.append((p * powmod(q, mod - 2)) % mod)

    s = sum(c) % mod
    assert s == 0

    res = 0
    for i in range(5002):
        if i:
            parc = 0
            for j in range(n):
                if a[j] < i:
                    parc = (parc + c[j]) % mod
            res = (res + powmod(i, mod - 2) * parc) % mod

    return res


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = rational_sums(n, a, b)
    print(result)
