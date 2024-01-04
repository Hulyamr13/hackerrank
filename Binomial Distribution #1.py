# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

p = 4 / 5
n = 4


def binom(k, n, p):
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def prob(k):
    return binom(k, n, p)


if __name__ == '__main__':
    result = prob(3) + prob(4)
    print('%.3f' % result)

    result = prob(0) + prob(1)
    print('%.3f' % result)