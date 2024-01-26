# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

n, k = map(int, input().strip().split())
count = 0

for i in range(1, n + 1):
    for r in range(i + 1):
        if math.comb(i, r) > k:
            count += 1

print(count)
