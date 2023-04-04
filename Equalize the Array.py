import math
import os
import random
import re
import sys


#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Write your code here
def equalizeArray(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    return len(arr) - max_freq


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()