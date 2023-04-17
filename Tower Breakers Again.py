import os
import sys
from functools import reduce


# Helper function to calculate the nim-value of a pile
def setup_nim(n):
    i = 2
    t = 0
    if n % 2 == 0:
        t += 1
    while i * i <= n:
        while n % i == 0:
            if n % 2 == 1:
                t += 1
            n = n // i
        i += 1
    if n > 1 and n % 2 == 1:
        t += 1
    return t


# Main function to calculate the winner of each test case
def towerBreakers(arr):
    # Calculate the nim-value of each pile
    nim_values = list(map(setup_nim, arr))

    # Calculate the xor of all the nim-values
    xor = reduce(lambda x, y: x ^ y, nim_values)

    # If the xor is 0, player 2 wins, otherwise player 1 wins
    return 2 if xor == 0 else 1


# Driver code to read inputs and call the main function
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        arr_count = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = towerBreakers(arr)
        fptr.write(str(result) + '\n')
    fptr.close()