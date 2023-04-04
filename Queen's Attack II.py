def queensAttack(n, k, r_q, c_q, obstacles):
    # Initialize variables for the number of squares the queen can attack
    left = c_q - 1
    right = n - c_q
    up = n - r_q
    down = r_q - 1
    up_left = min(up, left)
    up_right = min(up, right)
    down_left = min(down, left)
    down_right = min(down, right)

    # Iterate over each obstacle and update the variables accordingly
    for r, c in obstacles:
        # Check if the obstacle is in the same row or column as the queen
        if r == r_q:
            if c < c_q:
                left = min(left, c_q - c - 1)
            else:
                right = min(right, c - c_q - 1)
        elif c == c_q:
            if r < r_q:
                down = min(down, r_q - r - 1)
            else:
                up = min(up, r - r_q - 1)
        # Check if the obstacle is on the same diagonal as the queen
        elif abs(r - r_q) == abs(c - c_q):
            if r < r_q and c < c_q:
                down_left = min(down_left, r_q - r - 1)
            elif r < r_q and c > c_q:
                down_right = min(down_right, r_q - r - 1)
            elif r > r_q and c < c_q:
                up_left = min(up_left, r - r_q - 1)
            else:
                up_right = min(up_right, r - r_q - 1)

    # Return the sum of the variables
    return left + right + up + down + up_left + up_right + down_left + down_right

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)
