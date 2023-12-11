#!/bin/python3

import os
import sys


def xorKey(x, queries):
    ans = []
    bitset = [None] * (1 << 16)
    for i in range(len(x)):
        if bitset[x[i]]:
            bitset[x[i]].append(i)
        else:
            bitset[x[i]] = [i]
    m = max(x)
    i = 0
    while m > 0:
        m >>= 1
        i += 1
    m = (1 << i) - 1
    allset = ((1 << 16) - 1) & m

    for q in queries:
        ideal = q[0] ^ allset
        for i in range(1 << 16):
            if inrange(bitset[i ^ ideal], q):
                ans.append(allset ^ i)
                break
    return ans


def inrange(a, q):
    if a:
        p = b_search(a, q[1] - 1)
        if p < len(a) and a[p] < q[2]:
            return True
        return False
    return False


def b_search(a, x):
    l = 0
    r = len(a)
    while l != r:
        m = l + (r - l) // 2
        if x > a[m]:
            l = m + 1
        else:
            r = m
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nq = input().split()

        n = int(nq[0])

        q = int(nq[1])

        x = list(map(int, input().rstrip().split()))

        queries = []

        for _ in range(q):
            queries.append(list(map(int, input().rstrip().split())))

        result = xorKey(x, queries)

        fptr.write('\n'.join(map(str, result)))
        fptr.write('\n')

    fptr.close()