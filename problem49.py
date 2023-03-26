import re

s = input()

# Find the first occurrence of a repeating alphanumeric character
match = re.search(r'([a-zA-Z0-9])\1+', s)

if match:
    print(match.group(1))
else:
    print("-1")