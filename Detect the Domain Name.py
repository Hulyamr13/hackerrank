# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pattern = r'(http|https)\://(www\.|ww2\.|)([a-zA-Z0-9\-\.]+)(\.[a-zA-Z]+)(/\S*)?'
regex = re.compile(pattern)

domain_names = set()
num_lines = int(input())

for _ in range(num_lines):
    line = input()

    matches = regex.finditer(line)

    for match in matches:
        domain = match.group(3) + match.group(4)
        domain_names.add(domain)

sorted_domains = sorted(domain_names)
result = ';'.join(sorted_domains)

print(result)
