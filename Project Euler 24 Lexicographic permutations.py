# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import factorial


def get_lexicographic_permutation(s, k):
    s = list(s)
    length = len(s)
    result = []

    k -= 1  # Adjust k to start from 0 index

    factorial_list = [factorial(i) for i in range(length)]

    for i in range(length):
        index = k // factorial_list[length - 1 - i]
        result.append(s.pop(index))
        k %= factorial_list[length - 1 - i]

    return ''.join(result)


if __name__ == '__main__':
    num_test_cases = int(input())
    test_cases = []
    for _ in range(num_test_cases):
        k = int(input())
        test_cases.append(k)

    input_string = "abcdefghijklm"

    for k in test_cases:
        result = get_lexicographic_permutation(input_string, k)
        print(result)
