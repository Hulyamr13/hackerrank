#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

n = int(input())
prime = [True] * (n + 1)
answer = 1

for p in range(2, n + 1):
    if prime[p]:
        for j in range(2 * p, n + 1, p):
            prime[j] = False

        e = 0
        j = p
        while j <= n:
            e += n // j
            j *= p

        answer = (answer * (1 + 2 * e)) % 1000007

print(answer)
