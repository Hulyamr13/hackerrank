# Enter your code here. Read input from STDIN. Print output to STDOUT
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            sign = (-1) ** i
            sub_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
            det += sign * matrix[0][i] * determinant(sub_matrix)
        return det

matrix = [
    [3, 0, 0, -2, 4],
    [0, 2, 0, 0, 0],
    [0, -1, 0, 5, -3],
    [-4, 0, 1, 0, 6],
    [0, -1, 0, 3, 2]
]

result = determinant(matrix)
print(result)
