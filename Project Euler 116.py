# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 10 ** 9 + 7

T = [
    [[1, 1],
     [1, 0]],

    [[1, 1, 0],
     [0, 0, 1],
     [1, 0, 0]],

    [[1, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1],
     [1, 0, 0, 0]]
]


def matrix_multiply(a, b):
    prod = [[0] * len(b[0]) for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                prod[i][j] = (prod[i][j] + a[i][k] * b[k][j]) % MOD

    return prod


def matrix_power(fib, n):
    if n == 1:
        return fib

    M = T[len(fib) - 2]
    fib = matrix_power(fib, n // 2)
    fib = matrix_multiply(fib, fib)

    if n % 2 != 0:
        fib = matrix_multiply(fib, M)

    return fib


def fibonacci(n, type):
    fib = T[type]
    fib = matrix_power(fib, n - 1)

    return (fib[0][0] - 1) % MOD


if __name__ == "__main__":
    q = int(input())

    for _ in range(q):
        n = int(input())

        R = fibonacci(n + 1, 0)
        G = fibonacci(n + 1, 1)
        B = fibonacci(n + 1, 2)
        res = (R + G + B) % MOD

        print(res)
