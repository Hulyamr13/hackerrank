def phi(X):
    ''' Euler's totient of X '''
    f = X
    p = 2
    while p <= X:
        if p * p > X:
            p = X
        if X % p == 0:
            f -= f // p
            while X % p == 0:
                X //= p
        p += 1
    return f


def divisors(X):
    ''' generates divisors of X in increasing order (with possible repeats) '''
    d = 1
    # divisors <= sqrt(X)
    while d * d <= X:
        if X % d == 0:
            yield d
        d += 1
    # divisors > sqrt(X)
    while d > 1:
        d -= 1
        if X % d == 0:
            yield X // d


def F(X):
    if X % 4 == 0:
        return G(X // 4)
    elif X % 2 == 0:
        return G(X // 2)
    else:
        return G(X)


def G(X):
    a = b = 0
    # get exponent of 2
    while X & 1 == 0:
        X >>= 1
        a += 1
    # get exponent of 5
    while X % 5 == 0:
        X //= 5
        b += 1
    return H(X), max(a, b)


def H(X):
    X *= 9
    for d in divisors(phi(X)):
        if pow(10, d, X) == 1:
            return d


for cas in range(int(input())):
    X = int(input())
    a, b = F(X)
    print(2 * a + b)
