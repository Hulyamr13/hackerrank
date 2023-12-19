#!/bin/python3

import os
import sys
import bisect

# Complete the solve function below.
def solve(a, w):
    b = [[0,0],[10000000000,10000000000]]
    for i in range(len(a)):
        g = [a[i],w[i]]
        bisect.insort(b,g)
        ind = b.index(g)
        if b[ind+1][0] != b[ind][0] and b[ind-1][0] != b[ind][0]:
            b[ind][1]+=b[ind-1][1]
            for j in range(ind+1,len(b)):
                if b[j][1] >b[ind][1]:
                    break
            b = b[:ind+1] + b[j:]
        elif b[ind+1][0] == b[ind][0]:
            b[ind][1]+=b[ind-1][1]
            if b[ind+1][1]>=b[ind][1]:
                b.remove(b[ind])
            else:
                b.remove(b[ind+1])
                for j in range(ind+1,len(b)):
                    if b[j][1]>b[ind][1]:
                        break
                b = b[: ind+1] + b[j: ]
        elif b[ind-1][0] ==b[ind][0]:
            b[ind][1] += b[ind-2][1]
            if b[ind-1][1] >= b[ind][1]:
                b.remove(b[ind])
            else:
                for j in range(ind+1,len(b)):
                     if b[j][1]>b[ind][1]:
                        break
                b = b[: ind+1] + b[j: ]
                b.remove(b[ind-1])
    return b[-2][1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        w = list(map(int, input().rstrip().split()))

        result = solve(a, w)

        fptr.write(str(result) + '\n')

    fptr.close()