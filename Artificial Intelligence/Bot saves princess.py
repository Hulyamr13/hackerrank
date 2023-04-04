def displayPathtoPrincess(n, grid):
    # Find the positions of the bot and the princess
    bot_pos = None
    princess_pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                bot_pos = (i, j)
            elif grid[i][j] == 'p':
                princess_pos = (i, j)

    # Calculate the differences between the bot and princess positions
    row_diff = princess_pos[0] - bot_pos[0]
    col_diff = princess_pos[1] - bot_pos[1]

    # Determine the directions to move in based on the differences
    directions = []
    if row_diff < 0:
        directions.extend(['UP'] * abs(row_diff))
    else:
        directions.extend(['DOWN'] * row_diff)
    if col_diff < 0:
        directions.extend(['LEFT'] * abs(col_diff))
    else:
        directions.extend(['RIGHT'] * col_diff)

    # Print out the directions
    print('\n'.join(directions))

m = int(input())
grid = []
for i in range(m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)