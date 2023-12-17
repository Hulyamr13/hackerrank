#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    def isSorted(arr, lo, hi):
        i = lo + 1
        while i <= hi:
            if arr[i] < arr[i - 1]:
                return False
            i += 1
        return True

    def exch(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    if isSorted(arr, 0, len(arr) - 1):
        print("yes")
    else:
        sortedArr = arr[:]
        sortedArr.sort()

        lIdx = 0
        while lIdx < len(arr) and arr[lIdx] == sortedArr[lIdx]:
            lIdx += 1

        rIdx = len(arr) - 1
        while rIdx >= 0 and arr[rIdx] == sortedArr[rIdx]:
            rIdx -= 1

        exch(lIdx, rIdx)
        if isSorted(arr, lIdx, rIdx):
            print("yes")
            print("swap %d %d" % (lIdx + 1, rIdx + 1))
        else:
            exch(lIdx, rIdx)
            seg = arr[lIdx:rIdx + 1]
            seg.reverse()
            if isSorted(seg, 0, len(seg) - 1):
                print("yes")
                print("reverse %d %d" % (lIdx + 1, rIdx + 1))
            else:
                print("no")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
