import numpy

# take input from user
arr = input().strip().split(' ')

# convert input list into numpy array
arr_np = numpy.array(arr, int)

# reshape the array into a 2D array of shape (3, 3)
arr_np = numpy.reshape(arr_np, (3, 3))

# print the result
print(arr_np)
