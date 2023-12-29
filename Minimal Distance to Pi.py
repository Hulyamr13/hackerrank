#!/bin/python3

import sys

min, max = input().strip().split(' ')
min, max = [int(min), int(max)]

p = 314159265358979323846264338327950288419716939937510

a = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1]
m = len(a)

con = [[1, a[0]], [a[1], a[0] * a[1] + 1]]
for i in range(2, m):
    con.append([con[i - 2][0] + a[i] * con[i - 1][0], con[i - 2][1] + a[i] * con[i - 1][1]])

subconU = [[1, 4], [2, 7], [3, 10], [4, 13], [5, 16], [6, 19]]
subconL = []

for i in range(0, len(con) - 2):
    if i % 2 == 0:
        for j in range(0, a[i + 2]):
            subconL.append([con[i][0] + j * con[i + 1][0], con[i][1] + j * con[i + 1][1]])
    else:
        for j in range(0, a[i + 2]):
            subconU.append([con[i][0] + j * con[i + 1][0], con[i][1] + j * con[i + 1][1]])
subconL.sort()
subconU.sort()

upperbds = []
lowerbds = []
locmin = min
locmax = max
totalshiftx = 0
totalshifty = 0
while lowerbds == []:
    for i in subconL:
        if i[0] >= locmin:
            if i[0] <= locmax:
                lowerbds.append(i)
    if lowerbds == []:
        k = 0
        while subconL[k][0] < locmin:
            k += 1
        k = k - 1
        locmin = locmin - subconL[k][0]
        locmax = locmax - subconL[k][0]
        totalshiftx = totalshiftx + subconL[k][0]
        totalshifty = totalshifty + subconL[k][1]
for i in lowerbds:
    i[0] = i[0] + totalshiftx
    i[1] = i[1] + totalshifty

locmin = min
locmax = max

totalshiftx = 0
totalshifty = 0
while upperbds == []:
    for i in subconU:
        if i[0] >= locmin:
            if i[0] <= locmax:
                upperbds.append(i)
    if upperbds == []:
        k = 0
        while subconU[k][0] < locmin:
            k += 1
        k = k - 1
        locmin = locmin - subconU[k][0]
        locmax = locmax - subconU[k][0]
        totalshiftx = totalshiftx + subconU[k][0]
        totalshifty = totalshifty + subconU[k][1]
for i in upperbds:
    i[0] = i[0] + totalshiftx
    i[1] = i[1] + totalshifty
lowerbds.sort()
upperbds.sort()

up = upperbds[-1]
down = lowerbds[-1]

denom = 0
num = 0
dist = 100
a = abs((up[1] * (10 ** 50)) - p * up[0])
b = abs((down[1] * (10 ** 50)) - p * down[0])

if a * down[0] < b * up[0]:
    denom = up[0]
    num = up[1]
else:
    denom = down[0]
    num = down[1]
print(str(num) + '/' + str(denom))