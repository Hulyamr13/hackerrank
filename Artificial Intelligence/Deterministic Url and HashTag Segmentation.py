import re

# load dictionary of common English words and numbers
with open('words.txt', 'r') as f:
    words = set(f.read().splitlines())

def segment_string(s):
    # remove www and extensions from domain name
    if s.startswith('www.'):
        s = s[4:]
    s = re.sub('\.[a-z]+', '', s)
    # remove # symbol from hashtag
    if s.startswith('#'):
        s = s[1:]
    # initialize list to store tokens
    tokens = []
    # split string into tokens
    while s:
        # find longest possible word or number from left side
        for i in range(len(s), 0, -1):
            if s[:i] in words or re.match('^[\d.]+$', s[:i]):
                tokens.append(s[:i])
                s = s[i:]
                break
        else:
            # no valid token found, output original string
            return s
    # join tokens with space and return
    return ' '.join(tokens)

# read number of test cases
n = int(input())

# process each test case
for i in range(n):
    s = input().strip().lower()
    result = segment_string(s)
    print(result)