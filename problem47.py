import re

regex_pattern = r"[,.]"   # regular expression pattern to match commas and dots

n = input()   # input string
result = re.split(regex_pattern, n)   # split the string using the pattern

for element in result:
    print(element)
