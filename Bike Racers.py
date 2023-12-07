#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bikeRacers' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY bikers
#  2. 2D_INTEGER_ARRAY bikes
#

from collections import deque

def bikeRacers(bikers, bikes):
    def show(matrix):
        for row in matrix:
            print(str(row))

    def cost(r, b):
        dx = b[0] - r[0]
        dy = b[1] - r[1]
        return dx * dx + dy * dy

    def check(limit):
        rtob = {r: [b for b in range(m) if c[r][b] <= limit] for r in range(n)}
        assd_r = {}
        assd_b = {}
        assd = 0
        assdnow = True
        while assdnow:
            assdnow = False
            for r in range(n):
                if r not in assd_r:
                    paths = deque()
                    visited_r = set()
                    visited_r.add(r)
                    for b in reversed(rtob[r]):
                        paths.append([(r, b)])
                    while paths:
                        path = paths.pop()
                        rc, b = path[-1]
                        if b not in assd_b:
                            for rc, b in path:
                                assd_r[rc] = b
                                assd_b[b] = rc
                            assd += 1
                            if assd >= k:
                                return True
                            assdnow = True
                            break
                        else:
                            rc = assd_b[b]
                            if rc not in visited_r:
                                visited_r.add(rc)
                                for bc in reversed(rtob[rc]):
                                    if b != bc:
                                        np = path[:]
                                        np.append((rc, bc))
                                        paths.append(np)
        return False

    n, m, k = len(bikers), len(bikes), len(bikers[0])
    c = [[cost(bikers[r], bikes[b]) for b in range(m)] for r in range(n)]
    segs = sorted([c[r][b] for r in range(n) for b in range(m)])

    lo = 0
    hi = len(segs) - 1
    while lo < hi:
        mid = (hi + lo) // 2
        if check(segs[mid]):
            hi = mid
        else:
            lo = mid + 1
    return segs[lo]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])

    bikers = []
    for _ in range(n):
        bikers.append(list(map(int, input().rstrip().split())))

    bikes = []
    for _ in range(n):
        bikes.append(list(map(int, input().rstrip().split())))

    result = bikeRacers(bikers, bikes)

    fptr.write(str(result) + '\n')
    fptr.close()

