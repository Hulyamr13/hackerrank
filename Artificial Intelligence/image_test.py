def get_adjacent_cells(row, col):
    """Return a list of the 4 adjacent cells to (row, col)."""
    return [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

def expand_group(grid, visited, row, col):
    """Mark all cells in the group containing (row, col) as visited."""
    stack = [(row, col)]
    visited[row][col] = True
    while stack:
        r, c = stack.pop()
        for r2, c2 in get_adjacent_cells(r, c):
            if (0 <= r2 < len(grid) and 0 <= c2 < len(grid[0]) and
                not visited[r2][c2] and grid[r2][c2] == 1):
                stack.append((r2, c2))
                visited[r2][c2] = True

def count_groups(grid):
    """Return the number of groups of 1's in the grid."""
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if not visited[row][col] and grid[row][col] == 1:
                expand_group(grid, visited, row, col)
                count += 1
    return count

# Example usage:
grid = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
count = count_groups(grid)
print(count)
