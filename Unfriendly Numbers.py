#!/bin/python3

import os


# get greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER f
#

def solve(nums, f):
    # Initialize a list to store numbers that can divide f
    divisible = []

    # Output variable to count suitable divisors
    output = 0

    # Get all numbers that divide f
    bound = int(f ** 0.5)
    for i in range(1, bound + 1):
        if f % i == 0:
            divisible.append(i)
            if i != f // i:
                divisible.append(f // i)

    # Use gcd to get a new list of unique numbers from nums that can divide f
    new_unfriendly = []
    for num in nums:
        temp = gcd(num, f)
        if temp not in new_unfriendly:
            new_unfriendly.append(temp)

    # Find numbers in 'divisible' that do not divide any number in 'new_unfriendly'
    for num in divisible[1:]:
        is_divisible = False

        for unf_num in new_unfriendly:
            if unf_num % num == 0:
                is_divisible = True
                break

        if not is_divisible:
            output += 1

    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    f = int(first_multiple_input[1])

    nums = list(map(int, input().rstrip().split()))

    result = solve(nums, f)

    fptr.write(str(result) + '\n')

    fptr.close()
