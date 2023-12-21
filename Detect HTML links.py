import re

n = int(input())
regex = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'
for _ in range(n):
    s = input()
    links = re.findall(regex, s)
    for link, att in links:
        print('%s,%s' % (link, att.strip()))
