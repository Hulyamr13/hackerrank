import numpy as np

n, m, p = map(int, input().split())

# read in the arrays
array_1 = np.array([input().split() for _ in range(n)], int)
array_2 = np.array([input().split() for _ in range(m)], int)

# concatenate the arrays along axis 0
result = np.concatenate((array_1, array_2), axis=0)

print(result)
