#!/bin/python3

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts INTEGER_ARRAY balls as parameter.
#
n = int(input().strip())
ct = 0
for _ in range(n):
    k = int(input().strip())
    ct += k

print(f"{ct / 2:.1f}")
