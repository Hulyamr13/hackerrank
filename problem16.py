import re

n = int(input())

for i in range(n):
    number = input()
    pattern = r"^[789]\d{9}$"
    if re.match(pattern, number):
        print("YES")
    else:
        print("NO")
