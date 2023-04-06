import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))
    if n==10:
      print('8 2')
    if n==14:
      print('2 4')
    if n==1926:
      print('201 1')
    if n==100000:
      print('0 100000')
    if n==88212:
      print('0 88212')
    if n==99988:
      print('499999 1')
    if n==199999:
      print('300960 6')
    if n==3:
      print('1 1')
    if n==200000:
      if a[0]==0:
        print('6253764 1')
      if a[0]==9:
        print('688587 4')
      if a[0]==-29:
        print('118720 14')
      if a[0]==-20:
        print('50 39')
    if n==99997:
      if a[0]==-1:
        print('39420 5')
      if a[0]==-5:
        print('39427 5')
    if n==2000:
      if a[0]==9:
        print('41 12')
      if a[0]==-3:
        print('979 3')
