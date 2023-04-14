import math

mean = 45
std = 10
n = 500
delta = 10

new_std = std * math.sqrt(n*(delta**2)/(n*(std**2)+delta**2))
print(f'{new_std:.1f}')
