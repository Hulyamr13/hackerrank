#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    s = list(s)
    num = s[:]
    unpaired = len(list(filter(lambda x: x[0] != x[1], zip(num[:n // 2], reversed(num)))))

    if unpaired > k:
        return '-1'

    for i in range(n // 2):
        if unpaired < k and k >= 2:
            if num[i] != num[n - 1 - i]:
                unpaired -= 1
            if num[i] != '9':
                k -= 1
            if num[n - 1 - i] != '9':
                k -= 1
            num[i] = num[n - 1 - i] = '9'
            continue
        if num[i] == num[n - 1 - i]:
            continue
        k -= 1
        if k < 0:
            break
        num[i] = max(num[i], num[n - 1 - i])
        num[n - 1 - i] = num[i]

    if k > 0 and n % 2 == 1:
        num[n // 2] = '9'

    return '-1' if k < 0 else ''.join(num)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
