def is_safe(grid, row, col):
    # Check if placing a spy at grid[row][col] is safe

    # Check the row
    for i in range(col):
        if grid[row][i] == 'S':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if grid[i][j] == 'S':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(grid)), range(col, -1, -1)):
        if grid[i][j] == 'S':
            return False

    # Check for no three spies in a straight line
    for i in range(row - 2, -1, -1):
        if grid[i][col] == 'S' and grid[i + 1][col] == 'S' and grid[i + 2][col] == 'S':
            return False

    return True


def place_spies_util(grid, col):
    # Base case: If all spies are placed
    if col >= len(grid):
        return True

    for i in range(len(grid)):
        if is_safe(grid, i, col):
            grid[i][col] = 'S'

            # Recur to place spies for the next column
            if place_spies_util(grid, col + 1):
                return True

            # Backtrack if the placement does not lead to a solution
            grid[i][col] = '*'

    return False


def place_spies(N):
    # Create an empty grid
    grid = [['*' for _ in range(N)] for _ in range(N)]

    if place_spies_util(grid, 0):
        # Print the grid with spy positions
        print(N)
        for row in grid:
            print(" ".join(str(col + 1) for col, val in enumerate(row) if val == 'S'))
    else:
        print("No valid configuration found for N =", N)


# Example configurations for N = 11, 13, 7
place_spies(7)
place_spies(11)
place_spies(13)
