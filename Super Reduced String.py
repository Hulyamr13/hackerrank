#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # If the current character matches the top of the stack, remove it
        else:
            stack.append(char)  # Otherwise, add it to the stack
    if not stack:
        return "Empty String"
    else:
        return ''.join(stack)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
