import numpy

# take input from user
n, m = map(int, input().strip().split(' '))

# create a numpy array from input
arr = numpy.array([input().strip().split(' ') for _ in range(n)], int)

# transpose the array
arr_t = numpy.transpose(arr)

# flatten the array
arr_f = arr.flatten()

# print the results
print(arr_t)
print(arr_f)
