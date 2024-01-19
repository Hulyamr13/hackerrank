# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())
p_input = input().split()

x = 0
for i in range(m):
    x = int(p_input[x])
    if x >= n:
        x += (m - i - 1)
        break

print(x)
