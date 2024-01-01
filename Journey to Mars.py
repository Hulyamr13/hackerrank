from decimal import Decimal, getcontext

getcontext().prec = 50
log2 = Decimal(2).log10()
mod = 0


def decpart(x):
    return x - x.quantize(Decimal('1.'), rounding='ROUND_DOWN')


def fast_power(n):
    global mod
    if n <= 1:
        return 2 ** n

    c = fast_power(n // 2)
    c = c * c

    if n % 2 == 0:
        return c % mod

    return (2 * c) % mod


def first_digits(x, k):
    x = str(x).replace('.', '')
    return int(x[:k])


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n, k = map(int, input().split())
        mod = 10 ** k
        result = fast_power(n - 1) + first_digits(10 ** decpart(Decimal(n - 1) * log2), k)
        print(result)
