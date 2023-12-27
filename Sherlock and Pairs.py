#!/bin/python3

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

t = int(input())
for _ in range(t):
    ans = 0
    freq = [0] * 1000005

    n = int(input())
    numbers = list(map(int, input().split()))

    for x in numbers:
        freq[x] += 1

    for i in range(1, 1000001):
        ans += freq[i] * (freq[i] - 1)

    print(ans)

