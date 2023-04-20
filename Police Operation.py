import os
import sys


#
# Complete the policeOperation function below.
#
def cross(f, g):
    return (g[1] - f[1]) / (f[0] - g[0])


def policeOperation(h, criminals):
    n = len(criminals)
    dp = 0
    stack = []
    fpos = 0
    for i in range(0, n):
        f = [-2 * criminals[i], criminals[i] * criminals[i] + dp, 0]

        while len(stack) > 0:
            f[2] = cross(stack[-1], f)
            if stack[-1][2] < f[2]:
                break
            stack.pop()
            if len(stack) == fpos:
                fpos -= 1

        stack.append(f)
        x = criminals[i];
        while fpos + 1 < len(stack) and stack[fpos + 1][2] < x: fpos += 1
        dp = stack[fpos][0] * x + stack[fpos][1] + h + x * x;

    return dp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nh = input().split()

    n = int(nh[0])

    h = int(nh[1])
    result = 0
    if n != 0:
        criminals = list(map(int, input().rstrip().split()))
        result = policeOperation(h, criminals)

    fptr.write(str(result) + '\n')

    fptr.close()