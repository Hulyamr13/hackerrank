import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

sum_arr = numpy.sum(arr, axis=0)
product = numpy.prod(sum_arr)

print(product)