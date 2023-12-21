import re
import sys

x = sys.stdin.read()
comments = re.findall(r'(//.*?$|/\*.*?\*/)', x, re.MULTILINE | re.DOTALL)
for comment in comments:
    for line in comment.split('\n'):
        print(line.strip())
