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
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

erat = [1] * 100000
for i in range(2, int(len(erat) ** 0.5)):
    if erat[i]:
        for j in range(i * i, len(erat), i):
            erat[j] = 0

l, r = map(int, input().split())
p = [1] * (r - l + 1)
if l == 1:
    p[0] = 0

for d in range(2, len(erat)):
    if erat[d]:
        for i in range((l + d - 1) // d * d, r + 1, d):
            if i != d:
                p[i - l] = 0

c = sum(1 for i in range(len(p) - 2) if p[i] and p[i + 2])
print(c)
