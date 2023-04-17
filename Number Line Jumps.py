import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # If the second kangaroo is already ahead and moving faster, they will never meet
    if x2 > x1 and v2 >= v1:
        return "NO"
    # If the first kangaroo is already ahead and moving faster, they will never meet
    if x1 > x2 and v1 >= v2:
        return "NO"
    # Calculate the number of jumps needed for the kangaroos to meet
    jumps = (x2 - x1) / (v1 - v2)
    # If the number of jumps is a positive integer, they will meet
    if jumps > 0 and jumps.is_integer():
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()