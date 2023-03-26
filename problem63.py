from functools import reduce
from math import gcd

n = int(input())
nums = [tuple(map(int, input().split())) for _ in range(n)]

# multiply all the rational numbers using reduce()
product = reduce(lambda a, b: (a[0]*b[0], a[1]*b[1]), nums)

# simplify the resulting fraction by dividing both numerator and denominator by their gcd
divisor = gcd(product[0], product[1])
result = (product[0] // divisor, product[1] // divisor)

# print the resulting fraction in the required format
print(result[0], result[1])
