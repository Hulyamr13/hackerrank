#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n1
#  2. INTEGER k1
#  3. INTEGER n2
#  4. INTEGER k2
#  5. INTEGER n
#


def EulerPhi(n):
    phi = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            phi -= phi // i
        while n % i == 0:
            n = n // i
        if i != 2:
            i += 2
        else:
            i += 1
    if n > 1:
        phi -= phi // n
    return phi


def solve(n1, k1, n2, k2, n):
    if k1 == 0 or (n2 == 0 and k2 != 0):  # exponent is 0
        return pow(n1, 0, n)
    if n2 == 1 or k2 == 0:  # n2^k2 = 1
        return pow(n1, k1, n)
    if n1 == 0 or n1 % n == 0:  # exponent is not 0
        return 0
    if k2 == 1:  # other trivial case
        return pow(n1, k1 * n2, n)

    # Euler's theorem
    phi = EulerPhi(n)
    e = pow(n2, k2, phi) + phi
    return pow(pow(n1, k1, n), e, n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n1 = int(first_multiple_input[0])

        k1 = int(first_multiple_input[1])

        n2 = int(first_multiple_input[2])

        k2 = int(first_multiple_input[3])

        n = int(first_multiple_input[4])

        result = solve(n1, k1, n2, k2, n)

        fptr.write(str(result) + '\n')

    fptr.close()
