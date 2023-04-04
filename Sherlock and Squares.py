import math
import os
import random
import re
import sys


def squares(a, b):
    # count of square integers
    count = 0

    # iterate over the squares of integers within the range from a to b
    start = int(math.sqrt(a))
    end = int(math.sqrt(b)) + 1
    for i in range(start, end):
        square = i ** 2
        if square >= a and square <= b:
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()