# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input().strip())
i = 1

while True:
    p = pow(i, n)
    if len(str(p)) == n:
        print(p)
    if len(str(p)) > n:
        break
    i += 1
