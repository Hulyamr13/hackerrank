def is_valid_position(config, row, col):
    # Check if the position conflicts with any existing spies

    # Check same row
    if 'S' in config[row]:
        return False

    # Check same column
    for r in range(row):
        if config[r][col] == 'S':
            return False

    # Check diagonals
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if config[r][c] == 'S':
            return False
        r -= 1
        c -= 1

    r, c = row - 1, col + 1
    while r >= 0 and c < len(config[row]):
        if config[r][c] == 'S':
            return False
        r -= 1
        c += 1

    return True


def place_spies(config, row=0):
    # Base case: all rows have been filled
    if row == len(config):
        return True

    for col in range(len(config[row])):
        if is_valid_position(config, row, col):
            config[row][col] = 'S'
            if place_spies(config, row + 1):
                return True
            config[row][col] = '*'  # Backtrack

    return False


def print_configuration(config):
    num_spies = sum(row.count('S') for row in config)
    print(num_spies)
    spies = []
    for row in config:
        spy_positions = [i + 1 for i, cell in enumerate(row) if cell == 'S']
        spies.extend(spy_positions)
    print(' '.join(map(str, spies)))


# Main program
N = 13  # Size of the grid

# Create the grid
config = [['*' for _ in range(N)] for _ in range(N)]

# Place the spies
place_spies(config)

# Print the valid configuration
print_configuration(config)
