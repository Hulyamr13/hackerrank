#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    import heapq

    heapq.heapify(A)
    operations = 0

    while len(A) > 1 and A[0] < k:
        least_sweet = heapq.heappop(A)
        second_least_sweet = heapq.heappop(A)
        new_cookie = least_sweet + 2 * second_least_sweet

        heapq.heappush(A, new_cookie)
        operations += 1

    return operations if A[0] >= k else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
