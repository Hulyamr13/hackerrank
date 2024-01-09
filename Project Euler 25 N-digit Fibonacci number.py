# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import log10, ceil

def fibonacci_index(digits):
    if digits < 2:
        return 1
    golden_ratio = (1 + 5**0.5) / 2
    return ceil((digits + log10(5) / 2 - 1) / log10(golden_ratio))

if __name__ == "__main__":
    num_test_cases = int(input())
    test_cases = []
    for _ in range(num_test_cases):
        digits = int(input())
        test_cases.append(digits)

    for digits in test_cases:
        result = fibonacci_index(digits)
        print(result)
