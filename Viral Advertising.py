import math
import os
import random
import re
import sys


#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

# Write your code here
def viralAdvertising(n):
    shared = 5
    liked = 2
    cumulative = 2
    for _ in range(2, n + 1):
        shared = liked * 3
        liked = shared // 2
        cumulative += liked
    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()