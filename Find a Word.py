import re

sentences = [input() for _ in range(int(input()))]
targets = [input() for _ in range(int(input()))]

for target in targets:
    pattern = re.compile(r'(?:\W|\A)' + target + r'(?=\W|\Z)')
    print(sum(len(re.findall(pattern, sentence)) for sentence in sentences))
