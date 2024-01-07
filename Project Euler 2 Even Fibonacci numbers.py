#!/bin/python3

import sys


def fibonacci_sum_even(n):
    a, b = 1, 2
    total_sum = 0

    while b <= n:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b

    return total_sum


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        result = fibonacci_sum_even(n)
        print(result)