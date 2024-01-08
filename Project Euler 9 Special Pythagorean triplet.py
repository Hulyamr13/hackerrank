#!/bin/python3


def find_max_product(n):
    max_product = -1

    for a in range(1, n // 3):
        b = (n * n - 2 * n * a) // (2 * n - 2 * a)
        c = n - a - b

        if a * a + b * b == c * c:
            product = a * b * c
            if product > max_product:
                max_product = product

    return max_product


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        result = find_max_product(n)
        print(result)
