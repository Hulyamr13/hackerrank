import math
import os
import random
import re
import sys

def countSort(arr):
    n = len(arr)
    max_int = max(int(arr[i][0]) for i in range(n))
    counts = [[] for _ in range(max_int + 1)]

    for i in range(n):
        idx = int(arr[i][0])
        if i < n // 2:
            counts[idx].append("-")
        else:
            counts[idx].append(arr[i][1])

    result = []
    for i in range(max_int + 1):
        result.extend(counts[i])

    print(" ".join(result))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
