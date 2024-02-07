# Enter your code here. Read input from STDIN. Print output to STDOUT

def search(num_digits, multiplier, last_digit, modulo):
    shift = 10
    carry = 0
    current = last_digit
    result = last_digit

    while num_digits > 1:
        next_digit = multiplier * current + carry
        carry = next_digit // 10
        current = next_digit % 10

        if shift < modulo:
            result += current * shift
            shift *= 10

        num_digits -= 1

    first_digit = multiplier * current + carry

    if current == 0 or first_digit != last_digit:
        return 0

    return result

def main():
    max_digits = int(input().strip())
    modulo = 100000
    result = 0

    for num_digits in range(2, max_digits + 1):
        for multiplier in range(1, 10):
            for last_digit in range(1, 10):
                result += search(num_digits, multiplier, last_digit, modulo)

    print(result % modulo)

if __name__ == "__main__":
    main()
