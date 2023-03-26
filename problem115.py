import math


def dot_product(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def cross_product(a, b):
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

# take input

a = list(map(float, input().split()))
b = list(map(float, input().split()))
c = list(map(float, input().split()))
d = list(map(float, input().split()))

# find the normal vectors of the two planes
ab = [b[i] - a[i] for i in range(3)]
ac = [c[i] - a[i] for i in range(3)]
ad = [d[i] - a[i] for i in range(3)]
n1 = cross_product(ab, ac)
n2 = cross_product(ac, ad)

# find the angle between the normal vectors in degrees
cos_angle = dot_product(n1, n2) / (math.sqrt(dot_product(n1, n1)) * math.sqrt(dot_product(n2, n2)))
angle = math.degrees(math.acos(cos_angle))

# output the angle rounded to 2 decimal places
print("{:.2f}".format(angle))