
from itertools import groupby

s = input().strip()

# group consecutive characters and replace them with tuples of (count, character)
groups = [(len(list(g)), k) for k, g in groupby(s)]

# join the tuples with a space separator and concatenate the result
print(' '.join('({}, {})'.format(count, char) for count, char in groups))
