#!/bin/python3

import sys


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def largest_palindrome(n):
    largest_pal = 0

    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(product) and product < n and product > largest_pal:
                largest_pal = product

    return largest_pal


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        result = largest_palindrome(n)
        print(result)