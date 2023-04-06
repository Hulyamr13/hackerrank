import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Write your code here
def plusMinus(arr):
    n = len(arr)
    positive = sum(1 for x in arr if x > 0)
    negative = sum(1 for x in arr if x < 0)
    zero = sum(1 for x in arr if x == 0)
    print("{:.6f}".format(positive / n))
    print("{:.6f}".format(negative / n))
    print("{:.6f}".format(zero / n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
