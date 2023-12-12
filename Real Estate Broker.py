#!/bin/python3

import os
import sys

#
# Complete the realEstateBroker function below.
#
def realEstateBroker(clients, houses):
    #
    # Write your code here.
    #
    n = len(clients)
    m = len(houses)
    houses.sort()
    res = 0
    bought_clients = [False] * n
    for house in houses:
        x, y = house
        eligible_clients = [(clients[i][1], i) for i in range(n) if (not bought_clients[i]) and clients[i][0] < x and clients[i][1] >= y]
        if len(eligible_clients):
            p, j = min(eligible_clients)
            bought_clients[j] = True
            res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    clients = []

    for _ in range(n):
        clients.append(list(map(int, input().rstrip().split())))

    houses = []

    for _ in range(m):
        houses.append(list(map(int, input().rstrip().split())))

    result = realEstateBroker(clients, houses)

    fptr.write(str(result) + '\n')

    fptr.close()