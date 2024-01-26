# Enter your code here. Read input from STDIN. Print output to STDOUT

def summer(n):
    return sum([int(x) for x in str(n)])

n = int(input())
print(max([summer(i**j) for i in range(2, n) for j in range(1, n)]))
