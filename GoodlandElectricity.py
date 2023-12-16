import math
import os

def get_min(x, k, lights):
    best = -1
    best_ind = None
    for ind, i in enumerate(lights):
        if -k < x - i < k:
            best = i
            best_ind = ind
        elif i > x + k:
            break
    return best, best_ind

def pylons(k, arr):
    N = len(arr)
    lights = [i for i, val in enumerate(arr) if val == 1]
    pos = 0
    best = None
    best_ind = None
    count = 0

    while True:
        if pos >= N:
            break
        if best == lights[-1]:
            count = -1
            break
        if best_ind is None:
            best, best_ind = get_min(pos, k, lights)
        else:
            lights = lights[(best_ind + 1):]
            best, best_ind = get_min(pos, k, lights)
        if best == -1:
            count = -1
            break
        count += 1
        pos = best + k

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
