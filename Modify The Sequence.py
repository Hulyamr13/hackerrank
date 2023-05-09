#!/bin/python3

import math
import os
import random
import re
import sys

def longest_propper_subsequence(arr):
    N = len(arr)
    M = (N+1)*[0]

    L = 0
    for i in range(0,N):
        if arr[i] < i + 1:
            continue
        if arr[i] >= arr[M[L]] + i - M[L] :
            j = L+1
        else:
            lower = 1
            upper = L
            while lower <= upper:
                mid = int((upper+lower)/2)
                if arr[M[mid]] <= arr[i] - i + M[mid]:
                    lower = mid + 1
                else:
                    upper = mid - 1

            j = lower

        M[j] = i

        if j > L:
            L = j

    return L


def modifySequence(arr):
    L = longest_propper_subsequence(arr)
    return len(arr) - L


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()