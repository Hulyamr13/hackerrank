#!/bin/python3


import os
import sys

MOD = 1000000007

# Complete the solve function below.
def solve(a):
    def powmod(x, k, MOD):
        p = 1
        if k == 0:
            return p
        if k == 1:
            return x
        while k != 0:
            if k % 2 == 1:
                p = (p * x) % MOD
            x = (x * x) % MOD
            k //= 2
        return p

    answer = 1
    for i in a:
        answer *= powmod(2, i, MOD) + 1
        answer %= MOD
    return (answer - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()
