num = input()
e = int(input())

cipher = ''
for digit in num:
    shifted_digit = str((int(digit) + e) % 10)
    cipher += shifted_digit

print(cipher)
