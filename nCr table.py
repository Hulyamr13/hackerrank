#!/bin/python3

import os
from math import comb

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#


def solve(n):
    ncr = [comb(n, r) % 10**9 for r in range(n // 2 + 1)]
    return ncr + (ncr[:-1][::-1] if n % 2 == 0 else ncr[::-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
