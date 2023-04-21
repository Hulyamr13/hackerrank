import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    n = len(price)
    di = {price[i]:i for i in range(n)}
    price = sorted(price)
    m = 10000000
    for i in range(1, n):
        if di[price[i]] < di[price[i-1]]:
            m = min(m, price[i] - price[i-1])
    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
