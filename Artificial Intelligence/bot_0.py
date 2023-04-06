def displayPathToPrincess(n, grid):
    # find princess and mario
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
        if 'm' in row:
            mario = (idx, row.index('m'))

    # negative row difference implies UP
    # negative col difference implies LEFT
    drows = princess[0] - mario[0]
    dcols = princess[1] - mario[1]

    # Determine the directions to move in based on the differences
    directions = []
    if drows < 0:
        directions.extend(['UP'] * abs(drows))
    else:
        directions.extend(['DOWN'] * drows)
    if dcols < 0:
        directions.extend(['LEFT'] * abs(dcols))
    else:
        directions.extend(['RIGHT'] * dcols)

    # Print out the directions
    print('\n'.join(directions))

# org-babel variable check
if '_input' in globals():
    _input = _input.strip().split()
    m = int(_input[0], 10)
    grid = _input[1:]
else:
    m = input()
    grid = []
    for i in range(m):
        grid.append(input().strip())

displayPathToPrincess(m, grid)
