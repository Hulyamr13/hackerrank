import re

regex_pattern = r'^\d{2}(-(?:--)?|\.|:)\d{2}\1\d{2}\1\d{2}$'
test_string = input()

if re.match(regex_pattern, test_string):
    print("true")
else:
    print("false")
