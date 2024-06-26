#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findConnectedComponents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY d as parameter.
#

def findConnectedComponents(d):
    # Write your code here
    def count_components(i, prev_components, cliques):
        if i >= len(cliques):
            return len(prev_components)
        c = count_components(i + 1, prev_components, cliques)
        new_comp = cliques[i]
        components = []
        for comp in prev_components:
            if comp & new_comp:
                new_comp |= comp
            else:
                components.append(comp)
        if new_comp:
            components.append(new_comp)
        c += count_components(i + 1, components, cliques)
        return c

    singletons = [1 << j for j in range(64)]
    return count_components(0, singletons, d)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d_count = int(input().strip())

    d = list(map(int, input().rstrip().split()))

    components = findConnectedComponents(d)

    fptr.write(str(components) + '\n')

    fptr.close()
