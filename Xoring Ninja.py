import math
import os
import random
import re
import sys

def xoringNinja(arr):
    M = 1000000007
    n = len(arr)
    b0 = [0 for _ in range(32)]
    b1 = [0 for _ in range(32)]
    for k in range(n):
        for j in range(32):
            if(arr[k] & (1 << j)):
                tmp = b1[j]
                b1[j] = (b1[j] + 1 + b0[j]) % M
                b0[j] = (b0[j] + tmp) % M
            else:
                b1[j] = (b1[j] + b1[j]) % M
                b0[j] = (1 + b0[j] + b0[j]) % M

    cum = 0
    for j in range(32):
        val = ((1 << j) * b1[j]) % M
        cum = (cum + val) % M

    return cum

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        arr_count = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = xoringNinja(arr)
        print(result)
