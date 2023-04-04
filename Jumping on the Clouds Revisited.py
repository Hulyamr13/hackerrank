import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    i = k % n  # starting cloud after the first jump
    while i != 0:
        energy -= 1  # energy used for each jump
        if c[i] == 1:
            energy -= 2  # additional energy used if thunderhead
        i = (i + k) % n  # jump to next cloud
    if c[0] == 1:
        energy -= 2  # additional energy used to return to starting cloud if thunderhead
    energy -= 1  # last jump back to starting cloud
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
