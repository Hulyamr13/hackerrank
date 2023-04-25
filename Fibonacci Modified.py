def fibs(n, a, b):
    if n == 1:
        return a
    if n == 2:
        return b
    if fib[n] != 0:
        return fib[n]
    fib[n] = fibs(n - 1, a, b) ** 2 + fibs(n - 2, a, b)
    return fib[n]

fib = []
fib = fib + [0] * (21)


if __name__ == '__main__':
    line = input()
    inp = [int(x) for x in line.split(' ')]
    res = fibs(inp[2], inp[0], inp[1])
    print(res)
