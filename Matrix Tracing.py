import math
import os
import random
import re
import sys

mod = 10 ** 9 + 7


def getfactmod(b):
    val = 1
    for i in range(1, b):
        val = ((val % mod) * ((i + 1) % mod)) % mod
    return val


def getpowermod(a, b):
    result = 1
    while b:
        if b % 2 == 1:
            result = (result % mod * a % mod) % mod
        a = a % mod * a % mod
        b = b // 2
    return result


def solve(x, y):
    num = getfactmod(x + y - 2)
    denom = getfactmod(x - 1) * getfactmod(y - 1)
    return ((num % mod) * (getpowermod(denom, mod - 2))) % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()