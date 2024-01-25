# Enter your code here. Read input from STDIN. Print output to STDOUT

def p(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(p):
    a = (1 + 24 * p) ** 0.5
    return a == int(a) and (a + 1) % 6 == 0

n, k = map(int, input().split())
for i in range(k + 1, n):
    if is_pentagonal(p(i) - p(i - k)) or is_pentagonal(p(i) + p(i - k)):
        print(p(i))
