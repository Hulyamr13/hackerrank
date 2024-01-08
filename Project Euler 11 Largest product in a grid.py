#!/bin/python3

grid = []
for _ in range(20):
    grid.append(list(map(int, input().strip().split())))


def calculate_largest_product(grid):
    max_product = 0


    for i in range(20):
        for j in range(20 - 3):

            product = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
            max_product = max(max_product, product)


            product = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i]
            max_product = max(max_product, product)


    for i in range(20 - 3):
        for j in range(20 - 3):
            product = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
            max_product = max(max_product, product)


    for i in range(3, 20):
        for j in range(20 - 3):
            product = grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
            max_product = max(max_product, product)

    return max_product

result = calculate_largest_product(grid)
print(result)
