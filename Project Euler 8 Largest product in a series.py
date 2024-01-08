#!/bin/python3


def greatest_product_of_consecutive_digits(n, k, num):
    max_product = 0

    for i in range(n - k + 1):
        current_product = 1
        for j in range(i, i + k):
            current_product *= int(num[j])

        if current_product > max_product:
            max_product = current_product

    return max_product


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        n, k = map(int, input().strip().split())
        num = input().strip()

        result = greatest_product_of_consecutive_digits(n, k, num)
        print(result)