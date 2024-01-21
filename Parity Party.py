#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'parityParty' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#  4. INTEGER c
#

def parityParty(n, a, b, c):
    # Write your code here
    prime = 7340033
    m_poly = [0] * (a + b + 1)

    def fft(n, w, p):
        if n == 1:
            return p
        a = fft(n // 2, w * w % prime, p[0::2])
        b = fft(n // 2, w * w % prime, p[1::2])
        ret = [None] * n
        x = 1
        for k in range(n // 2):
            ret[k] = (a[k] + x * b[k]) % prime
            ret[k + n // 2] = (a[k] - x * b[k]) % prime
            x = x * w % prime
        return ret

    def multiply(n, p1, p2):
        w = pow(5, 2 ** 20 // n, prime)
        inv_w = pow(w, prime - 2, prime)
        a = fft(n, w, p1)
        b = fft(n, w, p2)
        p3 = [(a[i] * b[i]) % prime for i in range(n)]
        final = fft(n, inv_w, p3)
        inv_n = pow(n, prime - 2, prime)
        return [(x * inv_n) % prime for x in final]

    def vandermonde(m):
        return m_poly[m]

    def parityPartae(n, a, b, c):
        total = 0
        for m in range(a + b + 1):
            term = vandermonde(m)
            term = (term * pow(a + b + c - 2 * m, n, prime)) % prime
            total = (total + term) % prime
        return (total * pow(3670017, a + b, prime)) % prime

    biggy = max(a + 1, b + 1)
    poly_size = 1
    while poly_size < biggy:
        poly_size *= 2

    coeff = 1
    a_poly = [1]
    for i in range(poly_size - 1):
        if i < a:
            mult = (a - i)
            div = pow(i + 1, prime - 2, prime)
            coeff = (coeff * mult * div) % prime
            a_poly.append(-1 * coeff if i % 2 == 0 else coeff)
        else:
            a_poly.append(0)

    coeff = 1
    b_poly = [1]
    for i in range(poly_size - 1):
        if i < b:
            mult = (b - i)
            div = pow(i + 1, prime - 2, prime)
            coeff = (coeff * mult * div) % prime
            b_poly.append(coeff)
        else:
            b_poly.append(0)

    for i in range(poly_size):
        a_poly.append(0)
        b_poly.append(0)

    m_poly = multiply(2 * poly_size, a_poly, b_poly)
    result = parityPartae(n, a, b, c)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    a = int(first_multiple_input[1])

    b = int(first_multiple_input[2])

    c = int(first_multiple_input[3])

    result = parityParty(n, a, b, c)

    fptr.write(str(result) + '\n')

    fptr.close()
