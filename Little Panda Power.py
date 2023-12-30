modulo = 10**9 + 7

def power(base, exponent, mod=modulo):
    res = 1
    while exponent > 0:
        if exponent & 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exponent >>= 1
    return res


def egcd(a, b):
    if a == 0:
        return [b, 0, 1]
    ret = egcd(b % a, a)
    return [ret[0], ret[2] - ((b - b % a) // a) * ret[1], ret[1]]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B, X = map(int, input().split())
        if B < 0:
            ret = (X + egcd(A, X)[1]) % X
            print(power(ret, -B, X))
        else:
            print(power(A, B, X))
