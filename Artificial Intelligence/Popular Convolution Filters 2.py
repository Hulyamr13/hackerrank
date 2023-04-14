kernel1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
kernel2 = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
kernel3 = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
kernel4 = [[1/16, 1/8, 1/16], [1/8, 1/4, 1/8], [1/16, 1/8, 1/16]]
kernel5 = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
kernel6 = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

kernels = [kernel1, kernel2, kernel3, kernel4, kernel5, kernel6]

# Check each kernel
for i, kernel in enumerate(kernels, 1):
    is_identity = True
    for row in range(len(kernel)):
        for col in range(len(kernel[row])):
            if row == 1 and col == 1:
                continue  # skip the center pixel
            if kernel[row][col] != 0:
                is_identity = False
                break
        if not is_identity:
            break
    if is_identity:
        print(i)
        break
else:
    print("No identity kernel found.")
