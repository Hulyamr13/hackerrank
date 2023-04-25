#!/bin/python3

import os
import sys

#
# Complete the hackerrankCity function below.
#
def hackerrankCity(A):
    n=len(A)
    N=1
    dist=0
    sumd=A[0]*11#sum of all distances to the right bottom corner points
    dp=29*A[0]#dp is the sum of all distances
    for i in range(1,n):
        N=N*4+2
        dp=4*dp+sumd*(12*N+8)+A[i]*(16*N**2+12*N+1)
        dist=2*dist+3*A[i-1]
        sumd=4*sumd+A[i]*(8*N+3)+(3*N+2)*dist
        dp%=(10**9+7)
        sumd%=(10**9+7)
        N%=(10**9+7)
        dist%=(10**9+7)
    return dp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A_count = int(input())

    A = list(map(int, input().rstrip().split()))

    result = hackerrankCity(A)

    fptr.write(str(result) + '\n')

    fptr.close()