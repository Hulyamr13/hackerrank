#!/bin/python3

import math
import os
import random
import re
import sys


def entry(i, j):
    i = i % 7
    j = j % 7
    p = (i * i * j * j) % 7
    foo = [1, 1, 0, 1, 0, 0, 1, 1]
    return foo[p]


def rot90(n, i, j):
    return j, n + 1 - i


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    diff90 = 0
    diff180 = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            val0 = entry(i, j)
            i90, j90 = rot90(n, i, j)
            val90 = entry(i90, j90)
            i180, j180 = rot90(n, i90, j90)
            val180 = entry(i180, j180)

            if val0 != val90:
                diff90 += 1
            if val0 != val180:
                diff180 += 1

    for q_itr in range(q):
        angle = int(input().strip())
        angle = angle % 360

        if angle == 0:
            print(0)
        elif angle == 90 or angle == 270:
            print(diff90)
        elif angle == 180:
            print(diff180)
