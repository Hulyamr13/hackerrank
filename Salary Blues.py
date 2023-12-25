#!/bin/python3

import os
import sys


# Complete the solve function below.
def gcd(a, b):
    a = abs(a)
    b = abs(b)
    return gcd(b, a % b) if b else a


def solve(a, queries):
    n = len(a)

    d = 0
    for i in range(n):
        d = gcd(d, a[i] - a[0])

    result = []
    for k in queries:
        result.append(gcd(d, a[0] + k))

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = solve(a, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
