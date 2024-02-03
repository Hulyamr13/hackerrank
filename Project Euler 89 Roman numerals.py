# Enter your code here. Read input from STDIN. Print output to STDOUT

def roman_to_number(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    last = 0
    subtract = False
    for letter in reversed(roman):
        current = roman_values[letter]
        if current < last:
            subtract = True
            last = current
        elif current > last:
            subtract = False
            last = current
        if subtract:
            result -= current
        else:
            result += current
    return result

def number_to_roman(number):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ''
    for value, symbol in roman_numerals:
        while number >= value:
            result += symbol
            number -= value
    return result

# Input
test_cases = int(input())
romans = [input() for _ in range(test_cases)]

# Output
for roman in romans:
    number = roman_to_number(roman)
    print(number_to_roman(number))

