import re

s = input().strip()

matches = re.findall(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])', s)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)
