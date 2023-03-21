import re

n = int(input().strip())
t = []
a = re.compile(r'<[a-z0-9][\w._-]+@[a-z]+\.[a-z]{1,3}>', re.I)
for _ in range(n):
    t.append(input().strip())
for i, x in enumerate(t):
    v = a.search(x)
    if v:
        print(t[i])