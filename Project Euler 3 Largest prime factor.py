#!/bin/python3

import sys


def largest_prime_factor(n):
    max_prime = 1

    while n % 2 == 0:
        max_prime = 2
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n // i

    if n > 2:
        max_prime = n

    return max_prime


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        result = largest_prime_factor(n)
        print(result)