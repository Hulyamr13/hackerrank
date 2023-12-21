Regex_Pattern = r'^(Mr?s|[MDE]r)\.[a-zA-Z]+$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())