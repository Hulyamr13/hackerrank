#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    n = len(s)
    if n == 1:
        print("NO")
        return

    for i in range(1, n//2 + 1):
        first_num = int(s[:i])

        # Skip if first number has leading zero
        if s[0] == '0':
            continue

        temp = s[:i]
        while len(temp) < n:
            temp += str(first_num + 1)
            first_num += 1

        if temp == s:
            print("YES", s[:i])
            return

    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
