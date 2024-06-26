from bisect import *
import collections
from time import time
import random

popdistr = collections.Counter()


def naive(n, k):
    def gen(perm, nums):
        if len(perm) == n:
            perms.append(perm)
        for i in sorted(nums):
            if abs(perm[-1] - i) >= mindist:
                gen(perm + [i], nums - {i})

    perms = []
    mindist = n // 2
    for i in range(n):
        gen([i], set(range(n)) - {i})
    return perms[k] if k < len(perms) else -1


if 0:
    for k in range(7):
        print(naive(3, k))
    input()


def smart(n, k):
    if n < 5:
        return naive(n, k)

    half = n // 2
    h = half
    H = half + 1

    # Even n cases
    if not n & 1:
        if k > 1:
            return -1
        perm = [None] * n
        if k == 0:
            # 4 9 3 8 2 7 1 6 0 5
            perm[::2] = range(h - 1, -1, -1)
            perm[1::2] = range(n - 1, h - 1, -1)
        else:
            # 5 0 6 1 7 2 8 3 9 4
            perm[::2] = range(h, n)
            perm[1::2] = range(h)
        return perm

    low = (h + 3) << (h - 2)
    # low = 2 if n == 3 else (h + 3) << (h - 2)
    lowmid = 1 << (h - 1)
    # print(k, low, lowmid)
    if k >= (low + lowmid) * 2:
        return -1
    if k >= low + lowmid:
        merp = smart(n, (low + lowmid) * 2 - 1 - k)
        if merp == -2:
            return merp
        return [n - 1 - m for m in merp]
    if k >= low:
        return binary(list(range(n)), k - low, h)

    offset = [2]
    for i in range(half - 1):
        offset.append(offset[-1] * 2 + (1 << i))
        if offset[-1] > 10 ** 30:
            break
    offset.append(offset[-1] + (1 << (i + 1)))
    offset.append(0)  # offset[-1] = 0
    # print(offset)

    nums = list(range(n))
    perm = []
    pops = 0
    while True:

        # Cases k=0, k=1
        if k < 2:
            # n=11: 0 5 10 4 9 3 8 2 7 1 6
            #       0 6 1 7 2 8 3 9 4 10 5
            add = h + k
            return perm + [nums[i * add % n] for i in range(n)]

        i = bisect(offset, k)
        k -= offset[i - 1]

        # print(offset, i, k, end=' ... ')

        # Binary cases
        if k >= offset[i - 1]:  # or i == h:
            return perm + binary(nums, k - offset[i - 1], i)

        # Ugly cases
        perm += nums.pop(i), nums.pop(i + h - 1)
        n -= 2
        half -= 1
        h -= 1
        H -= 1

        if pops:
            popdistr[pops] -= 1
        pops += 1
        popdistr[pops] += 1


def binary(nums, k, i):
    n = len(nums)
    half = n // 2
    H = half + 1
    perm = [None] * n
    ks, testbit = bin(k)[:1:-1], half - 1
    left, right = 0, n - 1
    for m in range(i, i + half):
        if testbit < len(ks) and ks[testbit] == '1':
            perm[right] = nums[m]
            perm[right - 1] = nums[(m + H) % n]
            right -= 2
        else:
            perm[left] = nums[m]
            perm[left + 1] = nums[(m + H) % n]
            left += 2
        testbit -= 1
    perm[left] = nums[i + half]
    return perm


if 1:
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        perm = smart(n, k - 1)
        print(-1 if perm == -1 else ' '.join(str(p + 1) for p in perm))