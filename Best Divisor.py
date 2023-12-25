#!/bin/python3

import math
import os
import random
import re
import sys



def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def best_divisor(n):
    best_div = 1
    max_sum = 1
    for i in range(2, n + 1):
        if n % i == 0:
            current_sum = sum_of_digits(i)
            if current_sum > max_sum or (current_sum == max_sum and i < best_div):
                max_sum = current_sum
                best_div = i
    return best_div

if __name__ == '__main__':
    n = int(input().strip())
    result = best_divisor(n)
    print(result)