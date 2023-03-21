import re

n = int(input())
in_css = False

for i in range(n):
    line = input()

    if "{" in line:
        in_css = True
    elif "}" in line:
        in_css = False
    elif in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}', line):
            print(color)


