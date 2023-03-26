import numpy as np

n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)

min_vals = np.min(arr, axis=1)
result = np.max(min_vals)

print(result)