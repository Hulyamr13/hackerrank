#!/bin/python3

import os
import sys
from collections import deque

# Complete the substringDiff function below.
def substringDiff(k, s1, s2):
  longest = 0
  for d in range(-len(s1) + 1, len(s2)):
    i = max(-d, 0) + d
    j = max(-d, 0)
    q = deque(maxlen=k)
    s = 0
    for p in range(0, min(len(s2) - i, len(s1) - j)):
      if s1[i + p] != s2[j + p]:
        if k > 0:
          if len(q) == k:
            s = q[-1] + 1
          q.appendleft(p)
        else:
          s = p + 1
      if p + 1 - s > longest:
        longest = p + 1 - s
  return longest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        kS1S2 = input().split()

        k = int(kS1S2[0])

        s1 = kS1S2[1]

        s2 = kS1S2[2]

        result = substringDiff(k, s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()