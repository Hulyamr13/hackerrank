#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#
def get_primes(n):
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * int(((n - i * i - 1) / (2 * i) + 1))
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def waiter(number, q):
    # Write your code here
    bp = number[:]
    gp = []
    tp = []

    primes = get_primes(10000)
    p = 0
    current_prime = primes[0]

    while p < q:
        while bp:
            cur = bp.pop()
            if cur % current_prime == 0:
                gp.append(cur)
            else:
                tp.append(cur)

        p += 1
        current_prime = primes[p]

        while gp:
            yield gp.pop()

        bp = tp[:]
        tp.clear()

    while bp:
        yield bp.pop()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
