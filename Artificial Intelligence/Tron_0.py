
# Define a function to check if a move is valid
def is_valid_move(x, y, grid, move):
    if move == "LEFT":
        return y > 0 and grid[x][y - 1] == "-"
    elif move == "RIGHT":
        return y < 14 and grid[x][y + 1] == "-"
    elif move == "UP":
        return x > 0 and grid[x - 1][y] == "-"
    elif move == "DOWN":
        return x < 14 and grid[x + 1][y] == "-"
    else:
        return False

# Define a function to determine the next move for a player
def determine_next_move(player_x, player_y, grid):
    # First, try to move RIGHT if possible
    if is_valid_move(player_x, player_y, grid, "RIGHT"):
        return "RIGHT"
    # If not, try to move DOWN
    elif is_valid_move(player_x, player_y, grid, "DOWN"):
        return "DOWN"
    # If neither RIGHT nor DOWN is possible, move LEFT to prevent tracing back moves
    else:
        return "LEFT"


current_player = input().strip()
player_positions = list(map(int, input().strip().split()))
grid = [input().strip() for _ in range(15)]

# Extract player positions
player1_x, player1_y, player2_x, player2_y = player_positions

# Determine the next move for the current player
if current_player == "r":
    next_move = determine_next_move(player1_x, player1_y, grid)
else:
    next_move = determine_next_move(player2_x, player2_y, grid)

print(next_move)
