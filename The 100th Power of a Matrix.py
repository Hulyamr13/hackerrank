# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

A = [[1, math.pow(100, 1/100), 1, 0, 1]]

A_100 = [[math.floor(q**100) for q in row] for row in A]

for i in A_100:
    for q in i:
        print(q)
