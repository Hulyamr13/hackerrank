import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    # define character types
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    # initialize missing character types count
    missing_types = 0

    # check for presence of each character type
    if not any(c in numbers for c in password):
        missing_types += 1
    if not any(c in lower_case for c in password):
        missing_types += 1
    if not any(c in upper_case for c in password):
        missing_types += 1
    if not any(c in special_characters for c in password):
        missing_types += 1

    # calculate minimum number of characters to add
    if n < 6:
        return max(6 - n, missing_types)
    else:
        return missing_types

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
