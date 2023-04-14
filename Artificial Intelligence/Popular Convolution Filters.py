def is_blur_filter(kernel):
    """
    Checks if the given kernel is a blur filter or not.

    Parameters:
    kernel (list of lists): The kernel to be checked

    Returns:
    bool: True if the kernel is a blur filter, False otherwise
    """
    blur_filter = [[1 / 16, 1 / 8, 1 / 16], [1 / 8, 1 / 4, 1 / 8], [1 / 16, 1 / 8, 1 / 16]]

    # Check if the given kernel is same as the blur filter
    for i in range(3):
        for j in range(3):
            if abs(kernel[i][j] - blur_filter[i][j]) > 1e-9:
                return False

    return True


# Test the function with all the given filters
filters = [
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
    [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]],
    [[0, -1, 0], [-1, 5, -1], [0, -1, 0]],
    [[1 / 16, 1 / 8, 1 / 16], [1 / 8, 1 / 4, 1 / 8], [1 / 16, 1 / 8, 1 / 16]],
    [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]],
    [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
]

for i in range(6):
    if is_blur_filter(filters[i]):
        print(i + 1)