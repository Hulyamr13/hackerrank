#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#
def gridSearch(G, P):
    for i in range(len(G) - len(P) + 1):  # loop over rows of G
        for j in range(len(G[0]) - len(P[0]) + 1):  # loop over columns of G
            if G[i][j:j + len(P[0])] == P[0]:  # check if first row of P matches with current position in G
                match = True
                for k in range(1, len(P)):  # check if remaining rows of P match with corresponding rows in G
                    if G[i + k][j:j + len(P[0])] != P[k]:
                        match = False
                        break
                if match:
                    return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()