#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY roads
#  2. INTEGER_ARRAY machines
#

class Set:
    def __init__(self, city, machine):
        self.cities = set([city])
        self.machine = machine

def minTime(roads, machines):
    total = 0
    mach = set(machines)
    city_to_set, sets = dict(), dict()
    for c1, c2, t in sorted(roads, key=lambda x: x[2], reverse=True):
        # add new sets for the cities if they don't have one yet
        city_to_set[c1] = city_to_set.get(c1, Set(c1, c1 in mach))
        city_to_set[c2] = city_to_set.get(c2, Set(c2, c2 in mach))
        # get the sets
        s1, s2 = city_to_set[c1], city_to_set[c2]
        # if already in the same set, skip
        if s1 == s2:
            continue
        # if they both containe machines, add to total
        if s1.machine and s2.machine:
            total += t
            continue
        # 1 or less are machines, so merge the sets
        s1.cities.update(s2.cities)
        # update if combined set contains machines
        s1.machine = s1.machine or s2.machine
        # update the city to set mapping
        for c in s2.cities:
            city_to_set[c] = s1

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input().strip())
        machines.append(machines_item)

    result = minTime(roads, machines)

    fptr.write(str(result) + '\n')

    fptr.close()