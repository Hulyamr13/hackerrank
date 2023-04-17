import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    kaprekar_nums = []
    for num in range(p, q+1):
        square = str(num**2)
        d = len(str(num))
        r = square[-d:]
        l = square[:-d] or '0'
        if int(l) + int(r) == num:
            kaprekar_nums.append(num)
    if kaprekar_nums:
        print(' '.join(map(str, kaprekar_nums)))
    else:
        print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)