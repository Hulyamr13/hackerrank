import re

n = int(input())

for i in range(n):
    s = input()
    try:
        re.compile(s)
        print(True)
    except re.error:
        print(False)