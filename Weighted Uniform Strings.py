#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Create a set to store the weights of all uniform substrings
    weights = set()
    prev_char = ''
    count = 0

    # Iterate through the string and calculate the weights
    for char in s:
        if char == prev_char:
            count += 1
        else:
            count = 1
        weight = (ord(char) - ord('a') + 1) * count
        weights.add(weight)
        prev_char = char

    # Create an array to store the results
    result = []

    # Check if the weights are present in the set of uniform substring weights
    for query in queries:
        if query in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
