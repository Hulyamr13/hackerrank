import math
import os
import random
import re
import sys

def findPrt(a, prt):
    if prt[a] < 0:
        return a
    prt[a] = findPrt(prt[a], prt)
    return prt[a]

def join(a, b, prt):
    a = findPrt(a, prt)
    b = findPrt(b, prt)
    if a != b:
        prt[a] = b

def journeyToMoon(n, astronaut):
    # Additional code
    prt = [-1 for k in range(n)]
    for k in range(len(astronaut)):
        a, b = astronaut[k]
        join(a, b, prt)

    count = [0 for k in range(n)]
    for k in range(n):
        pk = findPrt(k, prt)
        count[pk] = count[pk] + 1
    return sum([a * (n - a) for a in count]) // 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
