def nextMove(n, r, c, grid):
    # Find the positions of the bot and the princess
    bot_pos = (r, c)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess_pos = (i, j)
                break

    # Determine the direction to move in to reach the princess
    if bot_pos[0] > princess_pos[0]:
        return 'UP'
    elif bot_pos[0] < princess_pos[0]:
        return 'DOWN'
    elif bot_pos[1] > princess_pos[1]:
        return 'LEFT'
    elif bot_pos[1] < princess_pos[1]:
        return 'RIGHT'
    else:
        return ''

# Read the input
n = int(input())
r, c = map(int, input().strip().split())
grid = [input() for _ in range(n)]

# Print the next move
print(nextMove(n, r, c, grid))