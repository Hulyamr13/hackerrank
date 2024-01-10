# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import factorial

def count_routes(n, m):
    return factorial(n + m) // (factorial(n) * factorial(m))

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    result = count_routes(n, m) % (10**9 + 7)
    print(result)
