# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import re

person = set(['**he**', '**him**', '**his**', '**she**', '**her**'])

texts = sys.stdin.readlines()
texts = [text.strip() for text in texts]
texts = [text for text in texts if text]
N = int(texts[0])
nouns = texts[-1].split(';')
texts = texts[1:-1]

corpus = ' '.join(texts)
corpus = re.sub('[.,!:;]', '', corpus)
words = corpus.split()

results = []
for i in range(len(words)):
    if words[i].startswith('**'):
        candidates = []
        for noun in nouns:
            length = len(noun.split())
            j = i - length
            while j >= 0 and ' '.join(words[j:j+length]) != noun:
                j -= 1
            if j >= 0:
                candidates.append((words[i], noun, j))
        results.append(candidates)

ppl = set()
for result in results:
    if len(result) == 1 and result[0][0] in person:
        ppl.add(result[0][1])

output = []
for result in results:
    if len(result) == 1:
        output.append(result[0][1])
    else:
        max_j = 0
        answer = None
        for can in result:
            if can[1] in ppl and can[0] not in person:
                continue
            if can[2] > max_j:
                answer = can[1]
                max_j = can[2]
        output.append(answer)

for out in output:
    print(out)
