import math
import os
import random
import re
import sys

def divisors(m):
    c = 0
    while m % 2 == 0:
        c += 1
        m = m // 2

    for i in range(3, int(m**0.5) + 1, 2):
        while m % i == 0:
            c += 1
            m = m // i
    if m > 2:
        c += 1
    return c

def towers(n):
    global memo
    nim_sum = 0
    for i in sorted(n):
        if i == 1:
            continue
        else:
            if i not in memo:
                memo[i] = divisors(i)
            nim_sum ^= memo[i]
    return nim_sum

memo = {}
def towerBreakers(arr):
    return 2 if towers(arr) == 0 else 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = towerBreakers(arr)

        fptr.write(str(result) + '\n')

    fptr.close()