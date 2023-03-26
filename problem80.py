import numpy

# set legacy print options for alignment
numpy.set_printoptions(legacy='1.13')

# read input values
n, m = map(int, input().split())

# create and print identity matrix
print(numpy.eye(n, m, k=0))
