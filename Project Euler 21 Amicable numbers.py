# Enter your code here. Read input from STDIN. Print output to STDOUT

MAX_NUM = 10**5

num_divisors = [0, 0] + [1] * MAX_NUM

divisor_sums = [0] * (MAX_NUM+1)

for factor in range(2, MAX_NUM // 2):
    for num in range(factor * 2, MAX_NUM + 1, factor):
        num_divisors[num] += factor

for i in range(1, MAX_NUM+1):
    divisor_sums[i] = divisor_sums[i-1]
    if num_divisors[i] <= MAX_NUM and num_divisors[i] != i and num_divisors[num_divisors[i]] == i:
        divisor_sums[i] += i

for _ in range(int(input())):
    n = int(input())
    print(divisor_sums[n])
