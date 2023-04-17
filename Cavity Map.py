def cavityMap(grid):
    n = len(grid)
    # Convert each row of the grid to a list of integers
    # to make it easier to work with the depths.
    depths = [list(map(int, row)) for row in grid]
    # Loop over all the inner cells of the grid.
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            # Check if the current cell is a cavity.
            if depths[i][j] > depths[i - 1][j] and \
               depths[i][j] > depths[i][j - 1] and \
               depths[i][j] > depths[i + 1][j] and \
               depths[i][j] > depths[i][j + 1]:
                # Replace the depth of the cavity with 'X'.
                grid[i] = grid[i][:j] + 'X' + grid[i][j+1:]
    return grid


if __name__ == '__main__':
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)
    print('\n'.join(result))