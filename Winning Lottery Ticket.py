import math
import os
import random
import re
import sys

def winningLotteryTicket(tickets):
    fullMask = 2**10-1
    cntMask = [0 for _ in range(fullMask+1)]

    for s in tickets:
        mask = 0
        for c in s:
            mask |= 1 << (ord(c) - ord('0'))
        cntMask[mask] += 1

    res = 0
    for i in range(fullMask+1):
        for j in range(i+1, fullMask+1):
            if i | j == fullMask:
                res += cntMask[i] * cntMask[j]

    res += cntMask[fullMask] * (cntMask[fullMask]-1) // 2
    return int(res)

if __name__ == '__main__':
    n = int(input().strip())
    tickets = []
    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)
    result = winningLotteryTicket(tickets)
    print(result)
