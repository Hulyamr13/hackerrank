# Enter your code here. Read input from STDIN. Print output to STDOUT

matrix1 = [
    [1, 2],
    [2, 3]
]

matrix2 = [
    [4, 5],
    [7, 8]
]

resultant_matrix = [[0, 0], [0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            resultant_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

for row in resultant_matrix:
    for element in row:
        print(element)
