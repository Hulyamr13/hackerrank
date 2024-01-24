# Enter your code here. Read input from STDIN. Print output to STDOUT

def convert(n, b):
    if n == 0:
        return '0'
    res = ''
    while n > 0:
        n, r = divmod(n, b)
        res = str(r) + res
    return res

def is_palindromic_in_both_bases(num, base):
    decimal_str = str(num)
    converted_str = convert(num, base)
    return decimal_str == decimal_str[::-1] and converted_str == converted_str[::-1]

def main():
    n, k = map(int, input().strip().split())
    total_sum = 0

    for i in range(1, n):
        if is_palindromic_in_both_bases(i, k):
            total_sum += i

    print(total_sum)

if __name__ == "__main__":
    main()
