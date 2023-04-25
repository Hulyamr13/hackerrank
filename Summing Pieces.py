#!/bin/python3

import os
import sys


#
# Complete the summingPieces function below.
#
def summingPieces(arr):
    #
    # Write your code here.
    #

    partialSum = 0  # this is the sum including last element
    count, total, coeff = 1, 0, 0
    for i in range(len(arr)):
        val = arr[i] % (10 ** 9 + 7)
        coeff += count
        coeff %= 10 ** 9 + 7
        total *= 2
        total %= 10 ** 9 + 7
        total += coeff * val + partialSum
        total %= 10 ** 9 + 7
        partialSum += count * val
        partialSum %= 10 ** 9 + 7
        count *= 2
        count %= 10 ** 9 + 7

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = summingPieces(arr)

    fptr.write(str(result) + '\n')

    fptr.close()