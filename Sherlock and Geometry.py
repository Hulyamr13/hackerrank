import os
from fractions import Fraction as F

def check(x1, y1, x2, y2, r):
    x, y = x1, y1
    dx = x2 - x
    dy = y2 - y
    A = dx**2 + dy**2
    halfB = x * dx + y * dy
    opt = F(-halfB, A)
    if opt < 0:
        opt = 0
    elif opt > 1:
        opt = 1
    least_dist = (x + dx * opt)**2 + (y + dy * opt)**2
    max_dist = max(x1**2 + y1**2, x2**2 + y2**2)
    return least_dist <= r**2 <= max_dist

def solve(x, y, r, t1, t2, t3):
    x1, y1 = t1[0] - x, t1[1] - y
    x2, y2 = t2[0] - x, t2[1] - y
    x3, y3 = t3[0] - x, t3[1] - y

    if check(x1, y1, x2, y2, r) or check(x2, y2, x3, y3, r) or check(x3, y3, x1, y1, r):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])
        y = int(first_multiple_input[1])
        r = int(first_multiple_input[2])

        t1 = list(map(int, input().rstrip().split()))
        t2 = list(map(int, input().rstrip().split()))
        t3 = list(map(int, input().rstrip().split()))

        result = solve(x, y, r, t1, t2, t3)

        fptr.write(result + '\n')

    fptr.close()
