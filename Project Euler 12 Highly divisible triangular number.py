# Enter your code here. Read input from STDIN. Print output to STDOUT

def count_divisors(n):
    divisors = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisors[j] += 1
    return divisors

def find_triangle_number(L, divisors):
    for n in range(1, len(divisors)):
        nDiv = divisors[n - 1] * divisors[n // 2] if n % 2 == 0 else divisors[(n - 1) // 2] * divisors[n]
        if nDiv > L:
            return (n - 1) * n // 2

num_tests = int(input())
max_number = 45000
divisors_list = count_divisors(max_number)
for _ in range(num_tests):
    L = int(input())
    result = find_triangle_number(L, divisors_list)
    print(result)
