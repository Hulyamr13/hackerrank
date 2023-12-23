# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_bijective(n, values):
    if len(values) != n:
        return "NO"

    for i in range(1, n + 1):
        if i not in values:
            return "NO"

    return "YES"


n = int(input())
values = list(map(int, input().split()))

result = is_bijective(n, values)
print(result)
