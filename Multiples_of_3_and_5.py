import math

def ans(n):
    # n * (n - 1) / 2
    three = 0
    first = 0
    five = 0
    second = 0
    extra = 0
    third = 0

    if n % 3 == 0:
        three = n // 3
        first = 3 * ((three * (three - 1)) // 2)
    else:
        three = n // 3
        first = 3 * ((three * (three + 1)) // 2)

    if n % 5 == 0:
        five = n // 5
        second = 5 * ((five * (five - 1)) // 2)
    else:
        five = n // 5
        second = 5 * ((five * (five + 1)) // 2)

    if n % 15 == 0:
        extra = n // 15
        third = 15 * ((extra * (extra - 1)) // 2)
    else:
        extra = n // 15
        third = 15 * ((extra * (extra + 1)) // 2)

    return first + second - third

t = int(input())
for a0 in range(t):
    n = int(input())
    print(ans(n))