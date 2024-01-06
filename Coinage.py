
#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY coins
#

modd = 10**9

def calculate_ways(n, a, b, c, d):
    ans = 0
    for i in range(min(d, n // 10) + 1):
        for j in range(min(c, n // 5) + 1):
            for k in range(min(b, n // 2) + 1):
                if 0 <= (n - 10 * i - 5 * j - 2 * k) <= a:
                    ans += 1
    return ans

T = int(input())
for _ in range(T):
    n = int(input())
    a, b, c, d = map(int, input().split())
    result = calculate_ways(n, a, b, c, d)
    print(result)
