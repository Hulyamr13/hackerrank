# Enter your code here. Read input from STDIN. Print output to STDOUT

def shift_digits(encoded_message):
    shifted_message = ''
    for digit in encoded_message:
        shifted_digit = str((int(digit) + 1) % 10)
        shifted_message += shifted_digit
    return shifted_message

encoded_message = input()
result = shift_digits(encoded_message)
print(result)
