# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import sys

s = sys.stdin.read()

Regex = r'question-summary-(\w\w\w\w\w)".*?class="question-hyperlink">(.+?)</a>.*?class=\"relativetime\">(.+?)</span>'
li = re.findall(Regex, s, re.DOTALL)

for a in li:
    print(';'.join(a))