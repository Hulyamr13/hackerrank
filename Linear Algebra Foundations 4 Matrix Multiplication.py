# Enter your code here. Read input from STDIN. Print output to STDOUT

# Define the matrices
matrix1 = [
    [1, 2, 3],
    [2, 3, 4],
    [1, 1, 1]
]

matrix2 = [
    [4, 5, 6],
    [7, 8, 9],
    [4, 5, 7]
]

resultant_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            resultant_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

for row in resultant_matrix:
    for element in row:
        print(element)
