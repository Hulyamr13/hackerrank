# Enter your code here. Read input from STDIN. Print output to STDOUT


import math

def get_digit_sum(number):
    digit_sum = 0
    while number != 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum

T = int(input())

for i in range(T):
    n = int(input())
    fact = math.factorial(n)
    print(get_digit_sum(fact))
