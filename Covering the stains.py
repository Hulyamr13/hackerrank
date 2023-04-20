#!/bin/python3

import os
import sys
def binomial(n,k):
    p=(n,k)
    if p in bin:
        return bin[p]
    if k==0 or k==n:
        return 1
    if k==1 or k+1==n:
        return n
    res= (binomial(n-1,k)+binomial(n-1,k-1))%mod
    bin[p]=res
    return res
bin={}
mod=1000000007
#
# Complete the coveringStains function below.
#
def coveringStains(k, coordinates):
    #
    # Write your code here.
    #
    n=len(coordinates)
    if k in [0,n]:
        return 1
    xmin=ymin=1111111
    xmax=ymax=-1
    for p in coordinates:
        x,y=p
        xmax=max(x,xmax)
        xmin=min(x,xmin)
        ymax=max(y,ymax)
        ymin=min(y,ymin)
    if xmin==xmax or ymin==ymax:
        res=  binomial(n-1,k-1)*2%mod
        if k>1:
            res-=binomial(n-2,k-2)
        return res%mod
    nx1=nx2=ny1=ny2=x1y1=x1y2=x2y1=x2y2=0
    for p in coordinates:
        x,y=p
        if x==xmin:
            nx1+=1
        if x==xmax:
            nx2+=1
        if y==ymin:
            ny1+=1
        if y==ymax:
            ny2+=1
        if x==xmin and y==ymin:
            x1y1+=1
        if x==xmin and y==ymax:
            x1y2+=1
        if x==xmax and y==ymin:
            x2y1+=1
        if x==xmax and y==ymax:
            x2y2+=1
        res=0
    for b in [nx1,nx2,ny1,ny2]:
        if k>=b:
            res+=binomial(n-b,k-b)
    for b in [nx1+nx2,ny1+ny2,nx1+ny1-x1y1,nx1+ny2-x1y2,nx2+ny1-x2y1,nx2+ny2-x2y2]:
        if k>=b:
            res-=binomial(n-b,k-b)
    for b in [nx1+ny1+nx2-x1y1-x2y1,nx1+ny2+nx2-x1y2-x2y2,ny1+nx1+ny2-x1y1-x1y2,ny1+nx2+ny2-x2y1-x2y2]:
        if k>=b:
            res+=binomial(n-b,k-b)
    b=nx1+ny1+nx2+ny2-x1y1-x2y1-x1y2-x2y2
    if k>=b:
        res-=binomial(n-b,k-b)
    return res%mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = coveringStains(k, coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()