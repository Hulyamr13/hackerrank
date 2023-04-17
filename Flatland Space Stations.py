import math
import os
import sys
from bisect import bisect_left

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    max_dist = 0
    for i in range(n):
        nearest = bisect_left(c, i)
        if nearest == len(c):
            max_dist = max(max_dist, i-c[nearest-1])
        elif nearest == 0:
            max_dist = max(max_dist, c[nearest]-i)
        else:
            max_dist = max(max_dist, min(i-c[nearest-1], c[nearest]-i))
    return max_dist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    fptr.write(str(result) + '\n')
    fptr.close()
