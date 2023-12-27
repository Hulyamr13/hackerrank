#!/bin/python3

import math
import os
import random
import re
import sys

def is_probable_prime(n, k = 7):
    if n < 6:
        return [False, False, True, True, False, True][n]
    if n & 1 == 0:
        return False
    s, d = 0, n - 1
    while d & 1 == 0:
        s, d = s + 1, d >> 1
    for a in random.sample(range(2, n - 2), min(n - 4, k)):
        x = pow(a, d, n)
        if x != 1 and x + 1 != n:
            for r in range(1, s):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                elif x == n - 1:
                    a = 0
                    break
            if a:
                return False
    return True

def f(n, k):
    if n < 2 * k:
        return False
    if k == 1:
        return is_probable_prime(n)
    if k == 2:
        if n % 2 == 0:
            return True
        else:
            return is_probable_prime(n - 2)
    return True

def solve(n, k):
    return "Yes" if f(n, k) else "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = solve(n, k)

        fptr.write(result + '\n')

    fptr.close()
