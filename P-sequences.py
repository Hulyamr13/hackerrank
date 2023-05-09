import math

def pSequences(n, p):
    P = 1000000007
    r = int(math.sqrt(p))

    f = [1] * (2 * r + 3)
    x = [1] * (2 * r + 3)
    y = [1] * (2 * r + 3)

    x[0] = 0

    max_val = r
    sum_val = r
    next_val = r

    while sum_val < p:
        f[max_val] = p // next_val - p // (next_val + 1)
        sum_val += f[max_val]
        next_val -= 1
        max_val += 1

    diff = 0
    if sum_val > p:
        max_val -= 1
        diff = 1

    while n > 0:
        for i in range(max_val, 0, -1):
            j = max_val - i + 1
            y[i] = (x[j] * f[j + diff] + y[i + 1]) % P

        x, y = y, x
        y[max_val + 1] = 0
        n -= 1

    return x[1]

if __name__ == '__main__':
    n = int(input().strip())
    p = int(input().strip())

    result = pSequences(n, p)

    print(result)
