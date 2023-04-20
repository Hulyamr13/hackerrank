import os
import sys


#
# Complete the travelAroundTheWorld function below.
#
def travelAroundTheWorld(a, b, c):
    total = 0
    n = len(a)
    city_num_to_validate = n
    for index in range(n - 1, -1, -1):
        tank = 0
        is_valid = True
        for i in range(city_num_to_validate):
            curr_index = (index + i) % n
            tank += a[curr_index]
            if tank > c:
                tank = c
            tank -= b[curr_index]
            if tank < 0:
                is_valid = False
                break
        if is_valid:
            total += 1
            city_num_to_validate = 1
        elif city_num_to_validate < n:
            city_num_to_validate += 1
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nc = input().split()

    n = int(nc[0])

    c = int(nc[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = travelAroundTheWorld(a, b, c)

    fptr.write(str(result) + '\n')

    fptr.close()