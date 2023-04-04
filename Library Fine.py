import math
import os
import random
import re
import sys


#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

# Write your code here
def libraryFine(d1, m1, y1, d2, m2, y2):
    # if the book is returned on or before the due date, no fine is charged
    if y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 <= d2):
        return 0
    # if the book is returned after the due date but in the same month and year, the fine is 15 * the number of days late
    elif y1 == y2 and m1 == m2:
        return 15 * (d1 - d2)
    # if the book is returned after the due month but in the same year, the fine is 500 * the number of months late
    elif y1 == y2:
        return 500 * (m1 - m2)
    # if the book is returned after the due year, the fine is fixed at 10000
    else:
        return 10000


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()