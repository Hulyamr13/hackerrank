import numpy as np

n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])

mean = np.mean(arr, axis=1)
var = np.var(arr, axis=0)
std = np.std(arr)

print(mean)
print(var)
print(round(std, 11))
