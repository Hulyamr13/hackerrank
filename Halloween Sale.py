#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Initialize the number of games bought and the current cost
    num_games = 0
    curr_cost = p

    # Buy games while there is still budget left
    while s >= curr_cost:
        # Buy a game and update variables
        num_games += 1
        s -= curr_cost

        # Update the cost of the next game
        curr_cost = max(curr_cost - d, m)

    return num_games


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()