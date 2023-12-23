# Enter your code here. Read input from STDIN. Print output to STDOUT

def find_inverse(n, values):
    inverse = [0] * n

    for i in range(n):
        inverse[values[i] - 1] = i + 1

    return inverse

n = int(input())
values = list(map(int, input().split()))

inverse_values = find_inverse(n, values)

for val in inverse_values:
    print(val)
