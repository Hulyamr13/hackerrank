import math
import os
import random
import re
import sys

def encryption(s):
    s = s.replace(" ", "") # remove spaces from string
    L = len(s)
    rows = int(math.sqrt(L)) # calculate number of rows
    cols = rows + 1 if rows * rows < L else rows # calculate number of columns
    encoded = ""
    for j in range(cols):
        for i in range(rows + 1):
            index = i * cols + j
            if index < L:
                encoded += s[index]
        encoded += " "
    return encoded.strip()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') if 'OUTPUT_PATH' in os.environ else sys.stdout

    s = input().strip()

    result = encryption(s)

    fptr.write(result + '\n')

    if fptr != sys.stdout:
        fptr.close()