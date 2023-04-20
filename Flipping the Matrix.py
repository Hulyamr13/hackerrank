def flippingMatrix(matrix):
    n = len(matrix)//2
    max_sum = 0
    for i in range(n):
        for j in range(n):
            max_sum += max(matrix[i][j], matrix[i][2*n - j - 1], matrix[2*n - i - 1][j], matrix[2*n - i - 1][2*n - j - 1])
    return max_sum

# Read number of queries
q = int(input().strip())

# Process each query
for _ in range(q):
    # Read matrix size
    n = int(input().strip())

    # Read matrix elements and convert them to integers
    matrix = []
    for _ in range(2*n):
        matrix.append(list(map(int, input().strip().split())))

    # Call flippingMatrix function and print the result
    result = flippingMatrix(matrix)
    print(result)
