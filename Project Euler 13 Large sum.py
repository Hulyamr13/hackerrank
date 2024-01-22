# Enter your code here. Read input from STDIN. Print output to STDOUT

def first_ten_digits_sum(N, numbers):
    total_sum = sum(int(number) for number in numbers)
    first_ten_digits = str(total_sum)[:10]
    return first_ten_digits


N = int(input())
numbers = []
for _ in range(N):
    number = input().strip()
    numbers.append(number)


result = first_ten_digits_sum(N, numbers)
print(result)
