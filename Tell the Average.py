# Enter your code here. Read input from STDIN. Print output to STDOUT

_, L = input(), list(map(int, input().split()))

result = 1
for b in L:
    result = (result * (b + 1)) % 1000000007

print((result - 1) % 1000000007)
