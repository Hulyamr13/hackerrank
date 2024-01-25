# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_triangular(x):
    return (1 + 8 * x) ** 0.5 == int((1 + 8 * x) ** 0.5)

def is_pentagonal(x):
    return (1 + 24 * x) ** 0.5 == int((1 + 24 * x) ** 0.5) and (int((1 + 24 * x) ** 0.5 + 1) % 6 == 0)

n, a, b = map(int, input().split())
limit = int((1 + 24 * n) ** 0.5 + 1) // 6 if a == 3 else int((1 + 8 * n) ** 0.5 + 1) // 4

for i in range(1, limit):
    num = i * (3 * i - 1) // 2 if a == 3 else i * (2 * i - 1)
    if is_triangular(num) if a == 3 else is_pentagonal(num):
        print(num)
