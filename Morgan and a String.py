import math
import os
import random
import re
import sys

def morganAndString(a, b):
    la = len(a)
    lb = len(b)
    a += "z"
    b += "z"
    i = j = 0
    res = ""
    while (i != la and j != lb):
        if a[i:] < b[j:]:
            res += a[i]
            i += 1
        else:
            res += b[j]
            j += 1

    res += a[i: -1] + b[j: -1]
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()
        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
