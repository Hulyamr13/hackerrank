#!/bin/python3

import math
import os
import random
import re
import sys


def one_solution(a, b, c):
    # find a pair of x, y such that x, y both integer, a*x + b*y = c
    A, B = a, b
    x = [1, 0, 0, 1]
    # a = a * x[0] + b * x[1]
    # b = a * x[2] + b * x[3]
    while b != 0:
        # a' = b
        # b' = a % b = a - (a // b) * b = a - q * b
        q = a // b
        a, b = b, a % b
        x = [x[2], x[3], x[0] - q * x[2], x[1] - q * x[3]]
    # now a == gcd(A, B) = A * x[0] + B * x[1]
    assert c % a == 0  # otherwise it's impossible
    q = c // a
    return q * x[0], q * x[1], a


def solve_y(a, b, c, x):
    return (c - a * x) // b


def sum_square(a, b):
    return a * a + b * b


def solve(a, b, c):
    x_0 = (a * c) // sum_square(a, b)

    x, y, g = one_solution(a, b, c)
    step_x = b // g  # the minimum step of x
    dist = ((x_0 - x) // step_x) * step_x
    x_smaller = x + dist
    while x_smaller + step_x <= x_0:
        x_smaller += dist
    x_bigger = x_smaller + step_x
    y_bigger = solve_y(a, b, c, x_bigger)
    y_smaller = solve_y(a, b, c, x_smaller)
    if x_smaller > 0:
        if sum_square(x_bigger, y_bigger) < sum_square(x_smaller, y_smaller):
            return [x_bigger, y_bigger]
        else:
            return [x_smaller, y_smaller]
    else:
        return [x_bigger, y_bigger]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = solve(a, b, c)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
