import re

N = int(input())
box = set()

for _ in range(N):
    s = input()
    regex_pattern = re.findall(r"<\s*([A-Za-z0-9]+)\s*>?", s)
    box.update(regex_pattern)

print(";".join(sorted(box)))
