#!/bin/python3

import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_on_house = 0
    oranges_on_house = 0

    for apple_dist in apples:
        apple_pos = a + apple_dist
        if apple_pos >= s and apple_pos <= t:
            apples_on_house += 1

    for orange_dist in oranges:
        orange_pos = b + orange_dist
        if orange_pos >= s and orange_pos <= t:
            oranges_on_house += 1

    print(apples_on_house)
    print(oranges_on_house)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)