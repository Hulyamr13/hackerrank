# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input().strip())

for _ in range(t):
    tn = int(input().strip())
    a = ((1 + 8 * tn) ** 0.5 - 1) / 2

    if a == int(a):
        print(int(a))
    else:
        print(-1)
