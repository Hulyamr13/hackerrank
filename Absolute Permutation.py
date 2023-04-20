import math
import os
import random
import re
import sys


def absolutePermutation(n, k):
    # If k = 0, the permutation is the sequence from 1 to n.
    if k == 0:
        return list(range(1, n + 1))

    # If n is odd or not divisible by k*2, there is no solution.
    if n % 2 == 1 or n % (k * 2) != 0:
        return [-1]

    result = []
    toggle = True

    for i in range(1, n + 1):
        if toggle:
            result.append(i + k)
        else:
            result.append(i - k)
        if i % k == 0:
            toggle = not toggle

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()