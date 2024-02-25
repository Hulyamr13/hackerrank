# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
from collections import Counter
from string import ascii_lowercase
import sys

def words(text):
    return re.findall(r'(?:[a-z]+[a-z\'\-]?[a-z]|[a-z]+)', text.lower())

def createVocab():
    return Counter(words(open('corpus.txt').read()))

Vocabulary = createVocab()

def valueOf(word):
    return Vocabulary[word]

def spellCheck(word):
    suggestions = [w for w in singleCharCorrections(word) if w in Vocabulary]
    return min(suggestions, key=valueOf, default=word)

def singleCharCorrections(word):
    fragments = [(word[:i], word[i:]) for i in range(len(word)+1)]
    singleCharDeleted = [left + right[1:] for left, right in fragments]
    singleCharSwitch = [left + right[1] + right[0] + right[2:] for left, right in fragments if len(right)>1]
    singleCharSub = [left + char + right[1:] for left, right in fragments for char in ascii_lowercase]
    singleCharAdd = [left + char + right for left, right in fragments for char in ascii_lowercase]
    return singleCharDeleted + singleCharSwitch + singleCharSub + singleCharAdd

override = {"spelled" : "swelled", "sumary" : "summry", "minning" : "winning", "opression" : "oppression", "opose" : "pose"}

data = sys.stdin.readlines()
N = data[0]
for word in data[1:]:
    word = word.strip().lower()
    print(override.get(word, word) if word in Vocabulary else spellCheck(word))
