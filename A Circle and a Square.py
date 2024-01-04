#!/bin/python3

import math
import os
import random
import re
import sys


def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def point_in_triangle(pt, v1, v2, v3):
    b1 = sign(pt, v1, v2) < 0
    b2 = sign(pt, v2, v3) < 0
    b3 = sign(pt, v3, v1) < 0
    return (b1 == b2 == b3)

def point_in_square(x, y, testx, testy):
    pt = (testx, testy)
    v1, v2, v3, v4 = (x[0], y[0]), (x[1], y[1]), (x[2], y[2]), (x[3], y[3])
    return point_in_triangle(pt, v1, v2, v3) or point_in_triangle(pt, v1, v3, v4)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    w = int(first_multiple_input[0])
    h = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    circleX = int(second_multiple_input[0])
    circleY = int(second_multiple_input[1])
    r = int(second_multiple_input[2])

    third_multiple_input = input().rstrip().split()

    x1 = int(third_multiple_input[0])
    y1 = int(third_multiple_input[1])
    x3 = int(third_multiple_input[2])
    y3 = int(third_multiple_input[3])

    xs = [x1 * 2, x1 * 2, x3 * 2, x3 * 2]
    ys = [y1 * 2, y3 * 2, y3 * 2, y1 * 2]

    x = (xs[0] + xs[2]) // 2
    y = (ys[0] + ys[2]) // 2

    xs[1] = x + (y - ys[0])
    ys[1] = y - (x - xs[0])

    xs[3] = x - (y - ys[0])
    ys[3] = y + (x - xs[0])

    for y in range(h):
        for x in range(w):
            c = '.'

            if (x - circleX) * (x - circleX) + (y - circleY) * (y - circleY) <= r * r:
                c = '#'
            elif point_in_square(xs, ys, x * 2, y * 2):
                c = '#'

            print(c, end='')
        print()
