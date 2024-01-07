#!/bin/python3

def sum_square_difference(n):
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
    square_of_sum = ((n * (n + 1)) // 2) ** 2
    return abs(sum_of_squares - square_of_sum)


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        result = sum_square_difference(n)
        print(result)