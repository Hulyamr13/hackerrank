#!/bin/python3

import os
import sys
import functools

#
# Complete the bobAndBen function below.
#
def bobAndBen(trees):
    #
    # Write your code here.
    #
    nims = []
    for tree in trees:
        nims.append(grundy(tree[0]))
    res = functools.reduce(lambda a,b: a^b, nims)
    if res == 0: return "BEN"
    return "BOB"

def grundy(m):
    res = 0 if m == 0 or m == 2 else ((m-1) % 2) + 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        trees = []

        for _ in range(n):
            trees.append(list(map(int, input().rstrip().split())))

        result = bobAndBen(trees)

        fptr.write(result + '\n')

    fptr.close()