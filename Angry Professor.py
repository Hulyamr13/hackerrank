import math
import os
import random
import re
import sys


def angryProfessor(k, a):
    # count the number of students who arrived on time or early
    on_time_students = sum(1 for x in a if x <= 0)

    # if the number of on-time students is less than k, class is cancelled
    if on_time_students < k:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()