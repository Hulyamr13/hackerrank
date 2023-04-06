import math
import os
import random
import re
import sys


def simpleArraySum(ar):
    # Инициализираме променлива със стойност 0, в която ще натрупваме сумата
    total = 0

    # Обхождаме списъка с числата и ги добавяме към натрупаната сума
    for num in ar:
        total += num

    # Връщаме като резултат натрупаната сума
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
