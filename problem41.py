import re

# read input strings
s = input().strip()
k = input().strip()

# find all matches of k in s and print their start and end indices
matches = re.finditer(r'(?={})'.format(re.escape(k)), s)
for match in matches:
    print('({}, {})'.format(match.start(), match.start() + len(k) - 1))

# if no match is found, print (-1, -1)
if not re.search(re.escape(k), s):
    print('(-1, -1)')
