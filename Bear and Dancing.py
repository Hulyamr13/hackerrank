import sys


numbers = input().split()

n, m = map(int, numbers[:2])
r = float(numbers[2])

states = {(0, 0, k): (0, 0) for k in range(max(n, m), n * m + 1)}

for s in range(1, n + m - 1):
    i = max(s - (m - 1), 0)
    while i < n and 0 <= s - i < m:
        j = s - i
        for k in reversed(range(max(n - i, m - j), (n - i) * (m - j) + 1)):
            a, b = 1, (k / (n * m)) * r
            if (i - 1, j - 1, k + 1) in states:
                a0, b0 = states[(i - 1, j - 1, k + 1)]
                c = i / n * j / m
                a += c * a0
                b += c * b0
            if (i - 1, j, k + 1) in states:
                a0, b0 = states[(i - 1, j, k + 1)]
                c = i / n * (1 - j / m)
                a += c * a0
                b += c * b0
            if (i, j - 1, k + 1) in states:
                a0, b0 = states[(i, j - 1, k + 1)]
                c = (1 - i / n) * j / m
                a += c * a0
                b += c * b0
            if (i, j, k + 1) in states:
                a0, b0 = states[(i, j, k + 1)]
                c = ((n - i) * (m - j) - k) / (n * m)
                a += c * a0
                b += c * b0

            a /= 1 - (k / (n * m)) * (1 - r)
            b /= 1 - (k / (n * m)) * (1 - r)
            states[(i, j, k)] = (a, b)
        # sys.stderr.write(f'{i=}, {j=}, {a=}, {b=}\n')

        i += 1

a, b = states[(n - 1, m - 1, 1)]
# sys.stderr.write(f'{a=}, {b=}\n')

print(f'{a / (1 - b) + 1}')