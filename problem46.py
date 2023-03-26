import re

# get the number of test cases
t = int(input())

for i in range(t):
    # get the input string
    n = input().strip()

    # check if the string is a valid floating point number
    if re.match(r'^[+-]?[0-9]*\.[0-9]+$', n):
        print("True")
    else:
        print("False")