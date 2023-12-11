#!/bin/python3

import os
import sys
from operator import xor
from itertools import accumulate
from collections import Counter

POW2 = 2 ** 16

#
# Complete the xorSubsequence function below.
#
xorSubsequence = lambda a: main(a)


# from wikipedia
def fwht(a) -> None:
    h = 1
    while h < len(a):
        for i in range(0, len(a), h * 2):
            for j in range(i, i + h):
                x = a[j]
                y = a[j + h]
                a[j] = x + y
                a[j + h] = x - y
        h *= 2


def main(seq):
    histogram = Counter(accumulate([0] + seq, xor))
    histogram = [histogram[value] for value in range(POW2)]

    fwht(histogram)
    histogram = [x * x for x in histogram]
    fwht(histogram)
    histogram = [y // POW2 for y in histogram]

    histogram[0] -= len(seq) + 1
    histogram = [y // 2 for y in histogram]
    max_freq = max(histogram)
    return next((i, freq) for i, freq in enumerate(histogram) if freq == max_freq)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = xorSubsequence(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()