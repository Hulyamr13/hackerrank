# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for _ in range(t):
    n = int(input())

    pow_val = pow(2, n)

    sum_digits = 0
    while pow_val > 0:
        digit = pow_val % 10
        sum_digits += digit
        pow_val //= 10

    print(sum_digits)
