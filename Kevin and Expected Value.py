#!/bin/python3

import os
from math import sqrt


#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts LONG_INTEGER n as parameter.
#

m = 5000500
a = [0.5 * (1 + sqrt(1 + 4 * i)) for i in range(m)]
a[0] = 0
for i in range(1, m):
    a[i] += a[i - 1]

def fair(n):
    return a[n - 1] / n

def unfair(n):
    return (0.5 * (n - 1) + 2 / 3 * (0.25 + n - 1) ** 1.5) / n

def solve(n):
    if n < m:
        return fair(n)
    else:
        return unfair(n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()
