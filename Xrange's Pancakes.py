#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY operations as parameter.
#

class Rotation:
    def __init__(self, n):
        self.a = 0
        self.f = False
        self.n = n

    def rotate(self, r):
        self.a = (self.a + r + self.n) % self.n

    def flip(self, t):
        self.f = not self.f
        self.a = (t - self.a + self.n) % self.n

    def print_rotation(self):
        if not self.f:
            print(1, self.n - self.a)
        else:
            print(2, self.a)


if __name__ == "__main__":
    n, m = map(int, input().split())
    rotation = Rotation(n)

    for _ in range(m):
        t, s = map(int, input().split())
        if t == 1:
            rotation.rotate(s)
        else:
            rotation.flip(s)

    rotation.print_rotation()

