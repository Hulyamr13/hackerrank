import numpy


def arrays(arr):
    # convert input list into numpy array
    arr_np = numpy.array(arr, float)

    # reverse the numpy array using slicing notation
    arr_np = arr_np[::-1]

    return arr_np


# take input from user
arr = input().strip().split(' ')

# call the function and print the result
result = arrays(arr)
print(result)
