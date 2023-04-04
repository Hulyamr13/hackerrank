import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

    # Write your code here
def climbingLeaderboard(ranked, player):
    ranks = []
    leaderboard = sorted(set(ranked), reverse=True)
    n = len(leaderboard)
    for score in player:
        while n > 0 and score >= leaderboard[n-1]:
            n -= 1
        ranks.append(n+1)
    return ranks



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
