import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

# Write your code here
def repeatedString(s, n):
    # count the number of a's in the original string
    a_count = s.count('a')

    # find the number of times the original string repeats fully in the first n characters
    full_repeats = n // len(s)

    # find the number of remaining characters that are part of an incomplete repeat
    partial_repeat_length = n % len(s)

    # count the number of a's in the remaining characters
    partial_a_count = s[:partial_repeat_length].count('a')

    # calculate the total number of a's in the first n characters
    total_a_count = a_count * full_repeats + partial_a_count

    return total_a_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()