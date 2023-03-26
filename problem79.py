import numpy as np

# read input values
n = int(input())
matrix = []
for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

# convert matrix to numpy array
matrix = np.array(matrix)

# calculate determinant
det = round(np.linalg.det(matrix), 2)

# print determinant
print(det)