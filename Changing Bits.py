#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'set_bit' function below.
#
# The function accepts following parameters:
#  1. INTEGER val
#  2. INTEGER i
#  3. BOOLEAN bit
#

def set_bit(val, i, bit):
    num = 1 << i

    if bit:
        return val | num

    return val & ~num

#
# Complete the 'changeBits' function below.
#
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#  3. STRING_ARRAY queries
#

def changeBits(a, b, queries):
    A = int(a, 2)
    B = int(b, 2)

    output = []
    for query in queries:
        split_input = query.split()

        command = split_input[0]
        index = int(split_input[1])

        if command == 'set_a':
            val = int(split_input[2])
            A = set_bit(A, index, val)

        elif command == 'set_b':
            val = int(split_input[2])
            B = set_bit(B, index, val)

        elif command == 'get_c':
            C = A + B
            C_bit = int(bool(C & (1 << index)))
            output.append(str(C_bit))

    print(''.join(output))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    ab_size = int(first_multiple_input[0])
    queries_size = int(first_multiple_input[1])

    a = input()
    b = input()

    queries = []

    for _ in range(queries_size):
        queries_item = input()
        queries.append(queries_item)

    changeBits(a, b, queries)
