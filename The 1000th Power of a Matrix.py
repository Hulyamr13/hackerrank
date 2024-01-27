def matrix_multiply(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_power(A, n):
    if n == 1:
        return A
    elif n % 2 == 0:
        half_power = matrix_power(A, n // 2)
        return matrix_multiply(half_power, half_power)
    else:
        return matrix_multiply(A, matrix_power(A, n - 1))

# Define the matrix A
A = [[-2, -9], [1, 4]]

# Calculate the 1000th power of A
A_1000 = matrix_power(A, 1000)

# Extract the elements A, B, C, D from the result
a, b = A_1000[0][0], A_1000[0][1]
c, d = A_1000[1][0], A_1000[1][1]

# Print the results
print(int(a))
print(int(b))
print(int(c))
print(int(d))
