#!/bin/python3

# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY steps as parameter.
#

n = int(input())

x = 100000000
y = 100000000

for _ in range(n):
    a, b = map(int, input().split())
    x = min(a, x)
    y = min(y, b)

print(x * y)

