import numpy as np

coefficients = list(map(float, input().split()))
x = float(input())

result = np.polyval(coefficients, x)
print(result)