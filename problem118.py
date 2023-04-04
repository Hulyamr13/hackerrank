import math
import os
import random
import re
import sys


def hurdleRace(k, height):
    # Find the maximum height of the hurdles
    max_height = max(height)

    # Calculate the difference between the character's maximum jump height and the maximum hurdle height
    diff = max_height - k

    # If the character can already clear all the hurdles, return 0
    if diff <= 0:
        return 0

    # Otherwise, calculate the number of doses required to clear the highest hurdle
    num_doses = math.ceil(diff)

    return num_doses


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
