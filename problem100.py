import cmath

z = complex(input().strip())

r = abs(z)
phi = cmath.phase(z)

print('{:.3f}'.format(r))
print('{:.3f}'.format(phi))